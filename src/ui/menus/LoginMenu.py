import os
from src.data.Users import Users
from src.ui.LoggedInScreen import LoggedInScreen


class LoginMenu:

    #gets user data
    strawhats = Users.getUsers()

    #If user is on the entering password part of the login menu
    onPassword = False

    #stores username
    username = ""

    #If user has put an invalid option on a incorrect username or password section of the login menu
    invalid = False

    choice = ""

    #login menu allowing user to input username and password to login
    @staticmethod
    def loginMenu(error=False):
        from src.ui.menus.MainMenu import MainMenu
        print()
        print("=======Login Menu=======")
        print()
        if not LoginMenu.onPassword:
            if error:
                print("\033[3m" + "Invalid Username" + "\033[3m")
                if LoginMenu.invalid: print("\033[3m" + "Please put an available option" + "\033[3m")
                print("[1] Try Again")
                print("[2] Return to Main Menu")
                LoginMenu.choice = input("")
                if (LoginMenu.choice == "1"):
                    LoginMenu.invalid = False
                    os.system("cls")
                    LoginMenu.loginMenu()
                elif (LoginMenu.choice == "2"):
                    LoginMenu.invalid = False
                    LoginMenu.onPassword = False
                    os.system("cls")
                    MainMenu.mainMenu()
                else:
                    LoginMenu.invalid = True
                    LoginMenu.reRunLoginMenu()
            else:
                LoginMenu.choice = input("Please enter your USERNAME: ")
        else:
            pass
        if LoginMenu.onPassword and not error:
            print("Please enter your USERNAME: " + LoginMenu.username)
        elif LoginMenu.checkUsername(LoginMenu.choice):
            LoginMenu.username = LoginMenu.choice
            LoginMenu.onPassword = True
        elif not LoginMenu.onPassword:
            LoginMenu.reRunLoginMenu()
        if not error: LoginMenu.choice = input("Please enter your PASSWORD: ")
        if error:
            print("\033[3m" + "Invalid Password" + "\033[3m")
            if LoginMenu.invalid: print("\033[3m" + "Please put an available option" + "\033[3m")
            print("[1] Try Again")
            print("[2] Password Hint")
            print("[3] Return to Main Menu")
            LoginMenu.choice = input("")
            if (LoginMenu.choice == "1"):
                os.system("cls")
                LoginMenu.invalid = False
                LoginMenu.loginMenu()
            elif(LoginMenu.choice == "2"):
                os.system("cls")
                LoginMenu.invalid = False
                print()
                print("Password Hint: Dream(1-3 words together)")
                print()
                print("press enter to continue")
                LoginMenu.choice = input()
                LoginMenu.reRunLoginMenu()
            elif (LoginMenu.choice == "3"):
                LoginMenu.invalid = False
                LoginMenu.onPassword = False
                os.system("cls")
                MainMenu.mainMenu()
            else:
                LoginMenu.invalid = True
                LoginMenu.reRunLoginMenu()
        elif LoginMenu.checkPassword(LoginMenu.choice):
            #logged in
            LoginMenu.onPassword = False
            os.system("cls")
            LoggedInScreen.printAsciiArt(LoginMenu.username.lower())
            print()
            print("press enter to go back to Main Menu")
            LoginMenu.choice = input()
            os.system("cls")
            MainMenu.mainMenu()
        else:
            LoginMenu.reRunLoginMenu()

    #checks if username user inputted is valid
    def checkUsername(username):
        if username.lower() in LoginMenu.strawhats:
            return True
        else:
            return False

    #checks if password user inputted is valid
    def checkPassword(password):
        if password.lower() == LoginMenu.strawhats[LoginMenu.username.lower()]["login"]:
            return True
        else:
            return False

    #reruns the login menu with error set to true running the incorrect section for either the password or username
    def reRunLoginMenu():
        os.system("cls")
        LoginMenu.loginMenu(True)


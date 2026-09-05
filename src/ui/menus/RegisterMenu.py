from random import choice

from src.data.Users import Users
import bcrypt
import os

from src.ui.LoggedInScreen import LoggedInScreen
from src.ui.menus.LoginMenu import LoginMenu


class RegisterMenu:

    choice = ""
    username = ""
    password = ""
    onPassword = False
    loginScreen = ""


    #register menu asking for user to input username and password
    def registerMenu(self, error = False): #error is for when a username is taken
        from src.ui.menus.MainMenu import MainMenu
        os.system("cls")
        print()
        print("=======Registration Menu=======")
        print()
        if not self.onPassword:
            self.username = ""
            if error: print("\033[3m" + "Username Taken" + "\033[3m")
            self.choice = input("Please enter a USERNAME: ")
            if not LoginMenu.checkUsername(self.choice):
                self.username = self.choice
                self.confirmation()
            else:
                self.registerMenu(True)
        else:
            pass
        print("Please enter a USERNAME: " + self.username)
        self.password = ""
        self.choice = input("Please enter a PASSWORD: ")
        self.password = self.choice
        self.confirmation()
        self.chooseScreen()
        self.register()
        self.onPassword = False
        os.system("cls")
        print()
        print("Registration Successful!")
        print()
        print("press enter to return to Main Menu")
        self.choice = input()
        MainMenu.mainMenu()

    # Store the hashed password and username in strawhat database
    def register(self):
        # Convert password to bytes and generate a secure salt
        # salt is a string that is added randomly to a password before hashing occurs
        pwd_bytes = self.password.encode("utf-8")
        salt = bcrypt.gensalt()
        # Hash the password
        self.password = bcrypt.hashpw(pwd_bytes, salt)
        Users.strawhats.update({f"{self.username}": {"login": self.password, "loginScreen": f"{self.loginScreen}"}})

    #user confirms if they keep the username and password they inputted
    def confirmation(self, error = False):
        from src.ui.menus.MainMenu import MainMenu
        os.system("cls")
        text = ""
        loginInput = ""
        if not self.onPassword:
            text = "USERNAME"
            loginInput = self.username
        if self.onPassword:
            text = "PASSWORD"
            loginInput = self.password
        print()
        print(f"{text}: {loginInput}")
        print(f"confirm {text.lower()}?")
        if error: print("\033[3m" + "Please put an available option" + "\033[3m")
        print()
        print("[1] confirm")
        print(f"[2] change {text.lower()}")
        print("[3] Return to Main Menu")
        choice = input()
        if choice == "1":
            os.system("cls")
            if self.onPassword: return ""
            self.onPassword = True
            self.registerMenu()
        elif choice == "2":
            self.registerMenu()
        elif choice == "3":
            self.onPassword = False
            MainMenu.mainMenu()
        else:
            os.system("cls")
            self.confirmation(True)

    #user chooses login screen for when they are logged in
    def chooseScreen(self, error = False):
        fullArt = []
        lineArt = ""
        print()
        print("Username and Password saved")
        print("Please choose a Login Screen")
        if error: print("\033[3m" + "Please put an available option" + "\033[3m")
        print()
        print("[1] Luffy\n[2] Zoro\n[3] Nami\n[4] Usopp\n[5] Sanji\n[6] Chopper\n[7] Robin\n[8] Franky\n[9] Brook\n[10] Jinbe\n[11] Custom")
        choice = input()
        if choice == "11":
            os.system("cls")
            print()
            print("Paste your Login Screen below")
            print("Type done on a new line when finished")
            while True:
                lineArt = input()
                if lineArt.lower() == "done":
                    break
                fullArt.append(lineArt)
            self.loginScreen = "\n".join(fullArt)
        elif int(choice) < 11 and int(choice) >0:
            self.loginScreen = LoggedInScreen.returnAsciiArt(int(choice))
        else:
            os.system("cls")
            self.chooseScreen(True)




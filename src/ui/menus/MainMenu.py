import os
import sys

from src.ui.menus.LoginMenu import LoginMenu
from src.ui.menus.RegisterMenu import RegisterMenu
from src.data.Users import Users


class MainMenu:
    #Welcome message only for when program starts for first time
    def welcomeMessage():
        print()
        print("Welcome to the Straw Hat Pirates Database!")

    #Main Menu method for the main menu of the program
    def mainMenu(error=False): #error is true when the user puts a wrong option
        os.system("cls")
        print()
        print("=======STRAW HAT PIRATES DATABASE=======")
        print()
        print("[1] Login")
        print("[2] Register")
        print("[3] Quit")
        if error: print("\033[3m" + "Please put an available option" + "\033[3m")
        choice = input("")
        if choice == "1":
            os.system("cls")
            LoginMenu.loginMenu()
        elif choice == "2":
            RegisterMenu().registerMenu()
            print(Users.getUsers())
        elif choice == "3":
            print("Thanks for using the program!")
            sys.exit(0)
        else:
            MainMenu.mainMenu(True)

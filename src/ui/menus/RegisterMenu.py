from src.data.Users import Users

class RegisterMenu:

    def registerMenu():
        RegisterMenu.register("hello","hola")



    def register(username, password):
        Users.strawhats.update({f"{username}": {"login": f"{password}"}})
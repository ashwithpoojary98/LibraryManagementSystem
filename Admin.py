class Admin:
    name = "Ashwith"
    password = "1234"

    def __init__(self):
        self.__name = 0
        self.__password = 0

    def admin_login(self):
        self.__name = input("Enter the UserName\n")
        self.__password = input("Enter the Password\n")
        if (self.__name == Admin.name) and (self.__password == Admin.password):
            print("Login Successful")
            return True
        else:
            print("Your Enter wrong Password or wrong Email")
        return False

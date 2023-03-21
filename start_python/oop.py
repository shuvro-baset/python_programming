class User:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            self.login = True
            print("Login Successful!")
        else:
            print("Login Failed!")

    def logout(self):
        self.login = False
        print("Logged Out!")

    def is_logged_in(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.is_logged_in():
            print(self.name, "-", self.email)
        else:
            print("User is not Logged in!")


user1 = User("Adam", "adam@testmail.com", "12345")

user1.login()
user1.profile()

hello = input()

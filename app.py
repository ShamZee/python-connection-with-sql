import sys
from dbhelper import DBhelper


class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)
        if user_input == '1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input('Enter your name :')
        email = input("Enter your email :")
        password = input('Enter your password :')

        response = self.db.register(name,email,password)
        if response:
            print('Resgistraion successful')
        else:
            print('Registraion Faild')
        self.menu()

    def login(self):
        email = input('Enter Email :')
        password = input('Enter password :')
        data = self.db.search(email,password)

        if len(data)==0:
            print('Incorrect email/password')
            self.login()
        else:
            print('Hello',data[0][1])
obj = Flipkart()
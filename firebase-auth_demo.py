import pyrebase
from getpass import getpass

firebaseConfig = {'apiKey': "AIzaSyBgXyDzMyO2EG3n1FhUDp9m9uacnnHlf6Y",
    'authDomain': "authpython-b780b.firebaseapp.com",
    'databaseURL': "https://authpython-b780b-default-rtdb.firebaseio.com",
    'projectId': "authpython-b780b",
    'storageBucket': "authpython-b780b.appspot.com",
    'messagingSenderId': "1069385851702",
    'appId': "1:1069385851702:web:20f836eec9f06a37d64997",
    'measurementId': "G-3PRDVNJYRP"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def __init__(self,api_key):
    self.api_key = api_key
    self.current_user = None
    self.credentials = credentials

def signUp():
    print("Signing Up...")
    email = input("Enter Email: ")
    password = getpass("Enter Password: ")
    user = auth.create_user_with_email_and_password(email,password)
    auth.send_email_verification(user['idToken'])
    print('email verification link send')
    try:
        print("New Account Created!")
        ask = input("Do you want to Login now?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already Exists")
        ask = input("Log in?[y/n]")
        if ask == 'y':
            login()

def login():
    print("Logging In...")
    email = input("Enter Email: ")
    password =getpass("Enter Password: ")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        print("Successfully Logged In")
        print(auth.get_account_info(login['idToken']))
    except:
        print("Invalid password")
        ask = input("do you want to reset password?[y/n]")
        if ask == 'y':
            auth.send_password_reset_email(email)
            print('Reset password link send')
        
      

ans=input("Are you a new user[y/n]")
if ans =='y':
      signUp()
elif ans =='n':
    login()
import pyrebase

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

def signUp():
    print("Signing Up...")
    email = input("Enter Email: ")
    password =input("Enter Password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("New Account Created!")
    except:
        print("Email already Exists")

def login():
    print("Logging In...")
    email = input("Enter Email: ")
    password =input("Enter Password: ")
    login = auth.sign_in_with_email_and_password(email,password)
    print("Successfully Logged In")

ans=input("Are you a new user[y/n]")
if ans =='y':
      signUp()
elif ans =='n':
    login()
import pyrebase

config = {
    "apiKey": "AIzaSyCcvukZwjr0SaTiAN77I-_iTuBTvTyB3p4",
    "authDomain": "debugthugs-syv.firebaseapp.com",
    "databaseURL": "https://debugthugs-syv-default-rtdb.firebaseio.com",
    "projectId": "debugthugs-syv",
    "storageBucket": "debugthugs-syv.appspot.com",
    "messagingSenderId": "446246027754",
    "appId": "1:446246027754:web:74ff1e343a97b6c50d3293",
    "measurementId": "G-7NHPZ8XQYY",
    "databaseURL": ""
} 

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = "test@gmail.com"
password = "123456"

user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)

# auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)
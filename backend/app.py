from flask import Flask, session, render_template, request, redirect, flash
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCcvukZwjr0SaTiAN77I-_iTuBTvTyB3p4",
    "authDomain": "debugthugs-syv.firebaseapp.com",
    "databaseURL": "https://debugthugs-syv-default-rtdb.firebaseio.com",
    "projectId": "debugthugs-syv",
    "storageBucket": "debugthugs-syv.appspot.com",
    "messagingSenderId": "446246027754",
    "appId": "1:446246027754:web:74ff1e343a97b6c50d3293",
    "measurementId": "G-7NHPZ8XQYY",
} 

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('login.html')

from firebase_admin import auth

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password) 
            session['user'] = email
            msg = email
            return render_template('landing.html', msg)
        except:
            return 'login failed'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user")
    return redirect('/login')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registration', methods=['POST','GET'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password) 
            session['user'] = email
            msg = email
            return render_template('landing.html', msg)
        except:
            return "signup failed"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
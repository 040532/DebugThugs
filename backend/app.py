from flask import Flask, session, render_template, request, redirect
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
    "databaseURL": ""
} 

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

app.secret_key = "secret"

@app.route('/', methods=['POST','GET'])
def index():
    if 'user' in session:
        return "Hi, {}".format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password) 
            session['user'] = email
        except:
            return "login failed"
    return render_template('index.html')

@app.route('/logout', methods=['POST','GET'])
def login():
    session.pop("user")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
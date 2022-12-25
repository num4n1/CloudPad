from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

config = {
    'apiKey': "AIzaSyAAmLS3iP7gqxILdBP4YeVmy1Fl4d0rRCk",
    'authDomain': "authenticate-chatbox.firebaseapp.com",
    'projectId': "authenticate-chatbox",
    'storageBucket': "authenticate-chatbox.appspot.com",
    'messagingSenderId': "2394197507",
    'appId': "1:2394197507:web:380f420d80c29f5ae64836",
    'measurementId': "G-T4BE6MH2DP",
    'databaseURL' : ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth() 

app.secret_key='secret'


@app.route('/api/login', methods=['POST','GET'])
def index():
    if('signedin'in session):
        return 'hi youre logged in'
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            signedin = auth.sign_in_with_email_and_password(email,password)
            session['signedin'] = email
        except:
            return 'Login credentials are incorrect'
    return render_template('login.html')


@app.route('/api/signup', methods=['POST','GET'])
def signuppage():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        try:
            new_user = auth.create_user_with_email_and_password(email,password)
            return 'Signup Succesful'
        except:
            return 'Signup failed'
    return render_template('signup.html')

@app.route('/api/logout')
def logout():
    session.pop('signedin')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
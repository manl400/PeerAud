from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from app import app, db

from .models import User


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


# Save e-mail to database and send to success page
@app.route('/showSignUp', methods=['POST'])
def signup():
    email = None
    if request.method == 'POST':
        real_name = request.form['inputName']
        email = request.form['inputEmail']
        user_password = request.form['inputPassword']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.user_email == email).count():
            reg = User(email, real_name, user_password)
            db.session.add(reg)
            db.session.commit()
            return render_template('index.html')
        else:
            return render_template('error.html')

    return render_template('index.html')


@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')
import os
import pymongo
from flask import Flask, redirect, url_for, render_template, request
from signup import signUpForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/signup', methods=['GET', 'POST'])
def registration():
    form = signUpForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'Your registration is complete!'
    return render_template('signup.html', form=form)


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()


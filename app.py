import os
import pymongo
from flask import Flask, redirect, url_for, render_template, request
from register import signUpForm

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/signup')
def signup():
    form = signUpForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'We confirm your registration!'
    return render_template("signup.html", form=form)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
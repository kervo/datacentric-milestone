from flask import Flask, redirect, url_for, render_template

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

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()


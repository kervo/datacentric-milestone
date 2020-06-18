import os
from flask import Flask, app, redirect, render_template, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.form import FlaskForm
from flask_pymongo import PyMongo
from forms import *
from bson.objectid import ObjectId


from os import path
from flask.helpers import flash
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')
app.config['SECRET_KEY'] = os.urandom(32)
# Variables for database
mongo = PyMongo(app)
users_files = mongo.db.usersfiles

'''MongoDB Variables'''
user = mongo.db.user
recipe = mongo.db.recipe
meal = mongo.db.dish_type


@app.route('/')
def index():
    return render_template("index.html", title='Wondercook')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = user
        registered_user = users.find_one({'username': request.form['username']})

        if registered_user:
            if checked_password_hash(registered_user['password'], request.form['password']):
                session['username'] = request.form['username']
                flash('Welcome to WonderCook')
                return redirect(url_for('dashboard'))
            
            else:
                flash('Wrong details, please try again')
                return redirect(url_for('login'))
        
        else:
            flash('This user does not exist, type your details again')
            return redirect(url_for('login'))
    return render_template("login.html", form=form, title='Log In')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/signup')
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

    '''
   if users_files in session:
        flash('This user is already registered')
        return redirect(url_for('/'))
        form = signUpForm()
        if form.validate_on_submit():
            users = users_files
            registered_user = users_files.find_one({'username': request.form['username']})

        if registered_user:
            flash("This user name already exists")
            return redirect(url_for('signup'))
        
        else:
            encrypted_password = generate_password_hash(request.form['password'])
            new_user = {
                "username": request.form['username'],
                "password": encrypted_password,
                "recipes": [],
            }
            users.insert_one(new_user)
            session["username"] = request.form['username']
            flash("You are ready to use wondercook")
            return redirect(url_for('dashboard'))
        '''
        


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
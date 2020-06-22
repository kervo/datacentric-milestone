import os
import math
import json
from flask import Flask, app, redirect, render_template, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.form import FlaskForm
import pymongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import *
from flask.helpers import flash
from pymongo.mongo_client import MongoClient

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'usersfiles'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')
app.config['SECRET_KEY'] = os.urandom(24) 
mongo = PyMongo(app)

from os import path
if path.exists("env.py"):
    import env

''' Connection with MongoDB'''
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "usersfiles"
COLLECTION_NAME1 = "dish_type"
COLLECTION_NAME2 = "recipes"
COLLECTION_NAME3 = "users"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# MongoDB Variables        
conn = mongo_connect(MONGODB_URI)
meal = conn[DBS_NAME][COLLECTION_NAME1]
recipe = conn[DBS_NAME][COLLECTION_NAME2]
user = conn[DBS_NAME][COLLECTION_NAME3]

@app.route('/')
def index():
    recipes = recipe.find({}, {"_id":0})
    for doc in recipes:
        print(doc)
    return render_template("index.html", doc=doc, title='WonderCook')

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
            return redirect(url_for('dashboard'))
    return render_template("login.html", form=form, title='Log In')
    
@app.route('/dashboard')
def dashboard():
    form = Add_RecipeForm()
    
    recipes = recipe.find({}, {"_id":0})
    for doc in recipes:
        return render_template("dashboard.html", doc=doc, title='Dashboard')

'''@app.route('/dashboard/<username>/page:<num>') 
def dashboard(username):
    if username is not None:
        my_recipes = recipe.find({
            'recipe_author_name': {'$regex': username, '$options': 'i'}
        })
        total_my_recipes = my_recipes.count()
        
    total_pages = range(1, math.ceil(total_my_recipes/8) + 1)
    skip_num = 8 * (int(num) - 1)
    recipes_per_page = my_recipes.skip(skip_num).limit(8).sort([("upvotes", -1)])
    
    if total_my_recipes <= 8:
        page_count = total_my_recipes
    elif (skip_num + 8) <= total_my_recipes:
        page_count = skip_num + 8
    else:
        page_count = total_my_recipes 
    return render_template("dashboard.html", recipes=recipe.find(), dishes=meal.find(), my_recipes=my_recipes, 
                    users=user.find(), total_pages=total_pages, num=num, skip_num=skip_num, 
                    page_count=page_count, total_my_recipes=total_my_recipes,
                    recipes_per_page=recipes_per_page, title='My WonderCook')
''' 

@app.route('/signup')
def signup():
    return render_template('signup.html', title='Sign Up')

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
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")        


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
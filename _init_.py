import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# Variables for database
mongo = PyMongo(app)
users_files = mongo.db.usersfiles

COLLECTION_NAME = "recipes"

users = [DBS_NAME]
recipes = [COLLECTION_NAME]


def mongo_connect(url):
    try:
        conn = PyMongo.MongoClient(url)
        return conn
    except PyMongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def mongo_connect(url):
    try:
        conn = PyMongo.MongoClient(url)
        return conn
    except PyMongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
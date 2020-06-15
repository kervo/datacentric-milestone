import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config['MONGODB_NAME'] = "usersfiles"
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# MONGODB_URI = os.getenv("MONGO_URI")

DBS_NAME = "usersfiles"
COLLECTION_NAME = "firstuser"

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
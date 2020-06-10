import os
from flask import Flask
from flask_pymongo import PyMongo
import pymongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

MONGODB_URI = os.getenv("MONGO_URI")

DBS_NAME = "usersfiles"
COLLECTION_NAME = "firstuser"

users = [DBS_NAME]
recipes = [COLLECTION_NAME]

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

from app import app

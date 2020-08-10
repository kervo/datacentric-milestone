import os
import pymongo
from flask import Flask

from os import path
if path.exists("env.py"):
    import env

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
        
conn = mongo_connect(MONGODB_URI)
meal = conn[DBS_NAME][COLLECTION_NAME1]
recipe = conn[DBS_NAME][COLLECTION_NAME2]
users = conn[DBS_NAME][COLLECTION_NAME3]
'''
documents = users.find()

for doc in documents:
    print(doc)
'''

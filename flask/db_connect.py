from credentials import mongodb_credentials
import pymongo
from pymongo import MongoClient

db_uri = "mongodb://" + mongodb_credentials["username"] + ":" + mongodb_credentials["password"] + "@" + mongodb_credentials["host"] + "/" + mongodb_credentials["db"]
db = MongoClient(db_uri)


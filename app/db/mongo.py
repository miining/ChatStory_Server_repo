from pymongo import MongoClient
import os

MONGO_URL = MongoClient(os.getenv("MONGO_URL"))
DB_NAME = os.getenv("DB_NAME", "chatstory")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()



MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.writers_platform
users_collection = db.users
posts_collection = db.posts
comments_collection = db.comments
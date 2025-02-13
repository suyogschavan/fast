# posts.py
from fastapi import APIRouter
from models import Post
from database import posts_collection

router = APIRouter()

@router.post("/")
def create_post(post: Post):
    post_dict = post.dict()
    posts_collection.insert_one(post_dict)
    return {"message": "Post created"}

@router.get("/")
def get_posts():
    posts = list(posts_collection.find())
    return posts

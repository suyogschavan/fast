from fastapi import APIRouter, Depends
from models import Post
from database import posts_collection
from dependencies import get_current_user
from bson import ObjectId

def serialize_document(doc):
    doc["_id"] = str(doc["_id"])
    return doc


router = APIRouter()

@router.post("/", dependencies=[Depends(get_current_user)])
def create_post(post: Post, current_user: dict = Depends(get_current_user)):
    post_dict = post.dict()
    post_dict["author_id"] = current_user["user_id"]
    posts_collection.insert_one(post_dict)
    return {"message": "Post created"}

@router.get("/", dependencies=[Depends(get_current_user)])
def get_posts(current_user: dict = Depends(get_current_user)):
    posts = list(posts_collection.find())
    return [serialize_document(i) for i in posts]
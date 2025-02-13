from fastapi import APIRouter
from models import Comment
from database import comments_collection

router = APIRouter()

@router.post("/{post_id}/comment")
def add_comment(comment: Comment):
    comments_collection.insert_one(comment.dict())
    return {"message": "Comment added"}

@router.get("/{post_id}/comments")
def get_comments(post_id: str):
    comments = list(comments_collection.find({"post_id": post_id}))
    return comments

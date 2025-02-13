from fastapi import APIRouter, Depends
from models import Comment
from database import comments_collection
from dependencies import get_current_user

router = APIRouter()

def serialize_document(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/{post_id}/comment", dependencies=[Depends(get_current_user)])
def add_comment(comment: Comment, current_user: dict = Depends(get_current_user)):
    comment_data = comment.dict()
    comment_data["author_id"] = current_user["user_id"]
    comments_collection.insert_one(comment_data)
    return {"message": "Comment added"}

@router.get("/{post_id}/comments", dependencies=[Depends(get_current_user)])
def get_comments(post_id: str, current_user: dict = Depends(get_current_user)):
    comments = list(comments_collection.find({"post_id": post_id}))
    return [ serialize_document(i) for i in comments]
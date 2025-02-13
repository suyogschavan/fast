from fastapi import APIRouter, Depends
from database import posts_collection
from dependencies import get_current_user

router = APIRouter()

@router.get("/", dependencies=[Depends(get_current_user)])
def search(q: str, current_user: dict = Depends(get_current_user)):
    posts = list(posts_collection.find({"title": {"$regex": q, "$options": "i"}}))
    return posts
from fastapi import APIRouter
from database import posts_collection

router = APIRouter()

@router.get("/")
def search(q: str):
    posts = list(posts_collection.find({"title": {"$regex": q, "$options": "i"}}))
    return posts
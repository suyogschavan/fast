# models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    password: str
    bio: Optional[str] = ""
    profile_pic: Optional[str] = ""

class Post(BaseModel):
    title: str
    content: str
    tags: List[str] = []
    author_id: str
    cover_image: Optional[str] = ""
    created_at: datetime = datetime.utcnow()

class Comment(BaseModel):
    post_id: str
    author_id: str
    text: str
    created_at: datetime = datetime.utcnow()

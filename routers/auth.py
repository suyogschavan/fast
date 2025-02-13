from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection
from utils import hash_password, verify_password, create_jwt

router = APIRouter()

@router.post("/signup")
def signup(user: User):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt({"user_id": str(user["_id"]), "email": user["email"]})
    return {"token": token}
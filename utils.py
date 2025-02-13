import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, Request

JWT_SECRET = "supersecretkey"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_jwt(data: dict) -> str:
    return jwt.encode({**data, "exp": datetime.utcnow() + timedelta(days=1)}, JWT_SECRET, algorithm="HS256")


# def get_current_user(request: Request):
#     token = request.headers.get("Authorization")
#     if not token:
#         raise HTTPException(status_code=401, detail="Token missing")
#     try:
#         token = token.split(" ")[1]  # Extract the token from 'Bearer <token>'
#         payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token expired")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")
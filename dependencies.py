from fastapi import HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta

JWT_SECRET = "supersecretkey"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Verify JWT Token
def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")
    try:
        token = token.split(" ")[1]  # Extract the token from 'Bearer <token>'
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

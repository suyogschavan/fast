import bcrypt
import jwt
from datetime import datetime, timedelta

JWT_SECRET = "supersecretkey"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_jwt(data: dict) -> str:
    return jwt.encode({**data, "exp": datetime.utcnow() + timedelta(days=1)}, JWT_SECRET, algorithm="HS256")
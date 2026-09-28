import jwt
from datetime import datetime, timedelta, timezone
from uuid import UUID
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

ACCESS_TOKEN_EXP = timedelta(minutes=30)
REFRESH_TOKEN_EXP = timedelta(days=7)

def create_access_token(user_id: UUID) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + ACCESS_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "access_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token

def create_refresh_token(user_id: UUID) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + REFRESH_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "refresh_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token
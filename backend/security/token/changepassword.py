import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

CHANGE_PASSWORD_EXP = timedelta(minutes=10)

def create_change_password_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + CHANGE_PASSWORD_EXP
    payload = {
        "sub": str(user_id),
        "typ": "change_password_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token
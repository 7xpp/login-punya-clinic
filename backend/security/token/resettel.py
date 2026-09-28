import jwt
from datetime import timedelta, datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

RESER_TEL_OTP_TOKEN_EXP = timedelta(minutes=10)
RESER_TEL_TOKEN_EXP = timedelta(minutes=10)

def create_reset_tel_otp_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESER_TEL_OTP_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_tel_otp_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token

def create_reset_tel_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESER_TEL_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_tel_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token
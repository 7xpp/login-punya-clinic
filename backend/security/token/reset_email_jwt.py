import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

RESET_EMAIL_TOKEN_OTP_EXP = timedelta(minutes=10)
RESET_EMAIL_TOKEN_EXP = timedelta(minutes=10)


def create_reset_email_otp_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESET_EMAIL_TOKEN_OTP_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_email_otp_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token

def create_reset_email_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESET_EMAIL_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_email_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire_token
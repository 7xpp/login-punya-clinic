import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_RESET_PASSWORD = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

RESET_PASSWORD_OTP_TOKEN_EXP = timedelta(minutes=10)
RESET_PASSWORD_TOKEN_EXP = timedelta(minutes=10)

def create_reset_password_otp_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESET_PASSWORD_OTP_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_password_otp_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY_RESET_PASSWORD, algorithm=ALGORITHM)
    return token, expire_token

def create_reset_password_token(user_id: str) -> tuple[str, datetime]:
    expire_token = datetime.now(timezone.utc) + RESET_PASSWORD_TOKEN_EXP
    payload = {
        "sub": str(user_id),
        "typ": "reset_password_token",
        "exp": expire_token
    }
    token = jwt.encode(payload, SECRET_KEY_RESET_PASSWORD, algorithm=ALGORITHM)
    return token, expire_token
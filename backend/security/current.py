from fastapi.security import APIKeyCookie
from fastapi import Depends, HTTPException, status, Request
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from dependencies.db import get_db
from crud.unitofwork import UnitOfWork
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

class RequireTokenType:

    def __init__(self, expected_type: str, cookie_name: str = None):
        self.expected_type = expected_type
        self.cookie_key = cookie_name or expected_type
        self.cookie_scheme = APIKeyCookie(name=self.cookie_key, auto_error=False)

    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        token = await self.cookie_scheme(request)

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ไม่สามารถยืนยันตัวตนได้",
            headers={"WWW-Authenticate": "Bearer"},
        )

        if not token:
            raise credentials_exception

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("sub")
            token_type: str = payload.get("typ")
            if not user_id or token_type != self.expected_type:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        with UnitOfWork(db) as uow:
            filter_user_id = uow.current_user.get_by_user_id(user_id)
            if not filter_user_id:
                raise credentials_exception
            return filter_user_id



get_access_token = RequireTokenType("access_token")
get_refresh_token = RequireTokenType("refresh_token")

get_change_password_token = RequireTokenType("change_password_token")

get_reset_password_otp_token = RequireTokenType("reset_password_otp_token")
get_reset_password_token = RequireTokenType("reset_password_token")

get_reset_email_otp_token = RequireTokenType("reset_email_otp_token")

get_reset_tel_otp_token = RequireTokenType("reset_tel_otp_token")
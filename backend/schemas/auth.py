from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class SignupRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    username: str
    email: EmailStr
    password: str
    confirmpassword: str
    tel: str

class SignupInDB(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    password: str
    tel: str
    created_at: datetime

class LoginRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    email: EmailStr
    password: str
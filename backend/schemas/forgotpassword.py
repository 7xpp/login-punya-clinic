from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ForgotPasswordOTPRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    otp: str

class ForgotPasswordOTPInDB(BaseModel):
    user_id: str
    otp: str
    otp_exp: datetime
    otp_is_revoked: bool = False
    reset_password_otp_token: str
    reset_password_otp_token_exp: datetime
    reset_password_otp_is_revoked: bool = False
    created_at: datetime

class ConfirmForgotPasswordRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    password: str
    confirmpassword: str
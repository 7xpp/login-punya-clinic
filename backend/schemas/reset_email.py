from datetime import datetime
from pydantic import BaseModel, ConfigDict, StringConstraints, EmailStr



class ResetEmailRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    password: str
    email: EmailStr

class ResetEmailCheckOTPRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    otp: str

class ResetEmailCheckOTPInDB(BaseModel):
    user_id: str
    otp: str
    otp_exp: datetime
    otp_is_revoked: bool = False
    reset_email_otp_token: str
    reset_email_otp_token_exp: datetime
    reset_email_otp_is_revoked: bool = False
    created_at: datetime
    email: str
    is_revoked: bool = False

class ConfirmResetEmailRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    email: EmailStr
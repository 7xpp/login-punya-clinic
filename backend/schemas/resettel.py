from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class ResetTelRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    password: str
    tel: str

class ResetTelCheckOTPRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    otp: str

class ResetTelCheckOTPInDB(BaseModel):
    user_id: str
    otp: str
    otp_exp: datetime
    otp_is_revoked: bool = False
    reset_tel_otp_token: str
    reset_tel_otp_token_exp: datetime
    reset_tel_otp_is_revoked: bool =False
    tel : str
    created_at: datetime
    is_revoked: bool = False
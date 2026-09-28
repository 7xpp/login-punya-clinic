from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ChangePasswordRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    password: str

class ChangePasswordInDB(BaseModel):
    user_id: str
    change_password_token: str
    change_password_token_exp: datetime
    change_password_token_is_revoked: bool = False
    created_at: datetime
    is_revoked: bool = False

class ChangePasswordConfirmRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    password: str
    confirmpassword: str
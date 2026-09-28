from pydantic import BaseModel, ConfigDict

class UserDetailRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    username: str
    
class UserDetailDataResponse(BaseModel):
    username: str
    email: str
    tel: str

class UserDetailDataResponse(BaseModel):
    data: UserDetailDataResponse
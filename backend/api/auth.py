from model.user import OLDUser
from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, Response
from crud.unitofwork import UnitOfWork
from service.auth import ServiceAuth
from schemas.auth import LoginRequest, SignupRequest
from security.current import get_access_token                       

router = APIRouter()

# ======================
# Signup
# ======================
@router.post("/signup")
def signup(user_input: SignupRequest, uow: UnitOfWork = Depends(get_uow)):
    signup_service = ServiceAuth(uow)
    result = signup_service.service_signup(user_input)
    return {"message": "สมัครสมาชิกสำเร็จ"}


# ======================
# Login
# ======================
@router.patch("/login",)
def login(user_input: LoginRequest, response: Response, uow: UnitOfWork = Depends(get_uow)):
    login_service = ServiceAuth(uow)
    result = login_service.service_login(user_input, response)
    return { "message": "เข้าสู่ระบบสำเร็จ"}


# ======================
# Logout
# ======================
@router.patch("/logout")
def logout(response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    logout_service = ServiceAuth(uow)
    result = logout_service.service_logout(current_user, response)
    return {"message": "ออกจากระบบสำเร็จ"}
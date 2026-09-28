from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, Response
from schemas.changepassword import ChangePasswordRequest, ChangePasswordConfirmRequest
from crud.unitofwork import UnitOfWork
from service.changepassword import ServiceChangePassword
from security.current import get_access_token, get_change_password_token
from model.user import OLDUser
from model.change_password import OLDResetPassword

router = APIRouter()

@router.post("/reset_password_password")
def reset_email(user_input: ChangePasswordRequest, response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    changepassword_service = ServiceChangePassword(uow)
    result = changepassword_service.service_changepassword(user_input, current_user, response)
    return { "message": "รหัสผ่านถูกต้อง" }

@router.patch("/reset_password")
def reset_password(user_input: ChangePasswordConfirmRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_change_password_token)):
    changepassword_service = ServiceChangePassword(uow)
    result = changepassword_service.service_confirm_changepassword(user_input, current_user)
    return { "message": "เปลี่ยนรหัสผ่านสำเร็จ" }
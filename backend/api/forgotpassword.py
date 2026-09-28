from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, Response
from schemas.forgotpassword import ForgotPasswordOTPRequest, ConfirmForgotPasswordRequest
from service.forgotpassword import ServiceFCC
from crud.unitofwork import UnitOfWork
from model.user import OLDUser
from model.forgot_password import OLDForgotPassword
from security.current import get_access_token, get_reset_password_otp_token, get_reset_password_token

router = APIRouter()

@router.post("/forgot_password")
def forgot_password(response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    forgotpassword_service = ServiceFCC(uow)
    result = forgotpassword_service.service_forgotpassword(current_user, response)
    return { "message": "ส่ง OTP สำเร็จ" }

@router.patch("/create_forgot_password_otp_again")
def create_forgot_password_otp_again(response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    createotpagain_service = ServiceFCC(uow)
    result = createotpagain_service.service_create_otp_again(current_user, response)
    return { "message": "ส่ง OTP สำเร็จ" }


@router.patch("/check_otp")
def check_otp(user_input: ForgotPasswordOTPRequest, response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_reset_password_otp_token)):
    checkotp_service = ServiceFCC(uow)
    result = checkotp_service.service_checkotp(user_input, current_user, response)
    return { "message": "OTP ถูกต้อง" }

@router.patch("/confirm_password")
def confirm_password(user_input: ConfirmForgotPasswordRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_reset_password_token)):
    confirmpassword_service = ServiceFCC(uow)
    result = confirmpassword_service.service_confirmpassword(user_input, current_user)
    return { "message": "เปลี่ยนรหัสผ่านสำเร็จ" }
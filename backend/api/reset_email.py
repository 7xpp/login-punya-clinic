from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, Response
from crud.unitofwork import UnitOfWork
from service.reset_email import ServiceResetEmail
from schemas.reset_email import ResetEmailRequest, ResetEmailCheckOTPRequest, ConfirmResetEmailRequest
from model.user import OLDUser
from model.reset_email import OLDResetEmail
from security.current import get_reset_email_otp_token, get_access_token

router = APIRouter()

@router.post("/reset_email")
def reset_email(user_input: ResetEmailRequest, response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    resetemail_service = ServiceResetEmail(uow)
    result = resetemail_service.service_reset_email(user_input, current_user, response)
    return { "message": "รหัส OTP ส่งไปยังอีเมลของคุณแล้ว" }

@router.patch("/create_reset_email_otp_again")
def create_reset_email_otp_again(response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    createotpagain_service = ServiceResetEmail(uow)
    result = createotpagain_service.service_create_otp_again(current_user, response)
    return { "message": "รหัส OTP ส่งไปยังอีเมลของคุณแล้ว" }
    
@router.patch("/check_otp_email")
def check_otp_email(response: Response, user_input: ResetEmailCheckOTPRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDResetEmail = Depends(get_reset_email_otp_token)):
    checkotp_service = ServiceResetEmail(uow)
    result = checkotp_service.service_check_otp(user_input, current_user, response)
    return { "message": "เปลี่ยนอีเมลสำเร็จ" }
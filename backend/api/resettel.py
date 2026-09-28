from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, Response
from crud.unitofwork import UnitOfWork
from service.resettel import ServiceResetTel
from schemas.resettel import ResetTelRequest, ResetTelCheckOTPRequest
from model.user import OLDUser
from model.resettel import OLDResetTel
from security.current import get_reset_tel_otp_token, get_access_token

router = APIRouter()

@router.post("/reset_tel")
def reset_tel(user_input: ResetTelRequest, response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    resettel_service = ServiceResetTel(uow)
    result = resettel_service.service_reset_tel(user_input, current_user, response)
    return { "message": "รหัส OTP ส่งไปยังอีเมลของคุณแล้ว" }

@router.patch("/create_reset_tel_otp_again")
def create_reset_tel_otp_again(response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    createotpagain_service = ServiceResetTel(uow)
    result = createotpagain_service.service_create_otp_again(current_user, response)
    return { "message": "รหัส OTP ส่งไปยังอีเมลของคุณแล้ว" }
    
@router.patch("/check_otp_tel")
def check_otp_tel(user_input: ResetTelCheckOTPRequest, response: Response, uow: UnitOfWork = Depends(get_uow), current_user: OLDResetTel = Depends(get_reset_tel_otp_token)):
    checkotp_service = ServiceResetTel(uow)
    result = checkotp_service.service_check_otp(user_input, current_user, response)
    return { "message": "ยืนยัน OTP สำเร็จ" }
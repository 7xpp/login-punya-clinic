from model.repair import OLDRepair
from dependencies.uow import get_uow
from email import message
from schemas.userdetail import UserDetailRequest, UserDetailDataResponse
from security.current import get_access_token
from service.userdetail import ServiceUserDetail
from crud.unitofwork import UnitOfWork
from model.user import OLDUser
from fastapi import APIRouter, Depends

router = APIRouter()

@router.patch("/edit_user_detail")
def edit_user_detail(user_input: UserDetailRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    edit_user_detail_service = ServiceUserDetail(uow)
    result = edit_user_detail_service.service_edit_user_detail(user_input, current_user)
    return { "message": "แก้ไขข้อมูลสำเร็จ" }
    
@router.get("/userdetail_response", response_model=UserDetailDataResponse)
def userdeta(current_user: OLDUser = Depends(get_access_token), uow: UnitOfWork = Depends(get_uow)):
    userdetail_service = ServiceUserDetail(uow)
    result = userdetail_service.service_userdetail(current_user)
    return { "data": result }
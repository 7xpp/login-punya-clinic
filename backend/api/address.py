from dependencies.uow import get_uow
from fastapi import APIRouter, Depends
from crud.unitofwork import UnitOfWork
from service.address import ServiceAdress
from security.current import get_access_token
from model.user import OLDUser
from model.address import OLDAddress
from schemas.address import AddressResponse, AddressRequest, EditAddressRequest, EditAddressResponseResponse, DeleteAddressResponseResponse

router = APIRouter()

# ======================
# Create Address
# ======================
@router.post("/address")
def create_address(user_input: AddressRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    address_service = ServiceAdress(uow)
    result = address_service.service_address(user_input, current_user)
    return { "message": "เพิ่มที่อยู่สำเร็จ" }

# ======================
# Response Address
# ======================
@router.get("/addressdatail", response_model=AddressResponse)
def response_address(uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    address_detail_service = ServiceAdress(uow)
    result = address_detail_service.service_address_detail(current_user)
    return { "data": result }

# ======================
# Response Edit Address
# ======================
@router.get("/edit_address_response/{id}", response_model=EditAddressResponseResponse)
def edit_address_response(id: str, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    edit_address_response_service = ServiceAdress(uow)
    result = edit_address_response_service.service_edit_address_response(current_user, id)
    return { "data": result }

# ======================
# Edit Address
# ======================
@router.patch("/edit_address/{id}")
def edit_address(id: str, user_input: EditAddressRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    edit_address_service = ServiceAdress(uow)
    result = edit_address_service.service_edit_address(user_input, current_user, id)
    return { "message": "แก้ไขที่อยู่สำเร็จ" }

# ======================
# Set Default Address
# ======================
@router.patch("/set_default_address/{id}")
def set_default_address(id: str, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    set_default_address_service = ServiceAdress(uow)
    result = set_default_address_service.service_set_default_address(current_user, id)
    return { "message": "ตั้งค่าที่อยู่สำเร็จ" }

# ========================
# Response Delete Address
# ========================
@router.get("/delete_address_response/{id}", response_model=DeleteAddressResponseResponse)
def service_delete_address_response(id: str, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    delete_address_response_service = ServiceAdress(uow)
    result = delete_address_response_service.service_delete_address_response(current_user, id)
    return { "data": result }

# ======================
# Delete Address
# ======================
@router.delete("/delete_address/{id}")
def delete_address(id: str, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    delete_address_service = ServiceAdress(uow)
    result = delete_address_service.service_delete_address(current_user, id)
    return { "message": "ลบที่อยู่สำเร็จ" }
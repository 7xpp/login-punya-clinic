from dependencies.uow import get_uow
from fastapi import APIRouter, Depends, UploadFile, File, Form
from schemas.repair import RepairRequest, RepairMultiFileRequest, RepairimgResponse, RepairResponse, ResponseAddressRepairResponse
from crud.unitofwork import UnitOfWork
from service.repair import ServiceRepair
from security.current import get_access_token
from model.user import OLDUser

router = APIRouter()

# ======================
# Upload Repair Image
# ======================
@router.post("/upload_img_repair", response_model=RepairimgResponse)
def create_img_repair(img_input: RepairMultiFileRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    repair_img_service = ServiceRepair(uow)
    result = repair_img_service.service_repair_img(img_input, current_user)
    return { "data" : result }

# ======================
# Response Address Repair
# ======================
@router.get("/response_address_repair", response_model=ResponseAddressRepairResponse)
def response_address_repair(uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    response_address_repair_service = ServiceRepair(uow)
    result = response_address_repair_service.service_response_address_repair(current_user)
    return { "data": result }

# ======================
# Create Repair
# ======================
@router.post("/repair")
def create_repair(user_input: RepairRequest, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    repair_service = ServiceRepair(uow)
    result = repair_service.service_repair(user_input, current_user)
    return { "message": "ส่งซ่อมสำเร็จ" }

# ======================
# Repair Response
# ======================
@router.get("/repair_response", response_model=RepairResponse)
def create_repair_response(uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    repair_response_service = ServiceRepair(uow)
    result = repair_response_service.service_repair_response(current_user)
    return { "data" : result }

# ======================
# Cancel Repair
# ======================
@router.patch("/cancel_repair/{id}")
def cancel_repair(id: str, uow: UnitOfWork = Depends(get_uow), current_user: OLDUser = Depends(get_access_token)):
    cancel_repair_service = ServiceRepair(uow)
    result = cancel_repair_service.service_cancel_repair(id, current_user)
    return { "message": "ยกเลิกสำเร็จ" }
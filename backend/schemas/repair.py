from pydantic import BaseModel, ConfigDict
from datetime import datetime
from schemas.status import StatusRepair
import uuid
from typing import Optional, List

# ======================
# Upload Repair Image
# ======================
class RepairFileRequest(BaseModel):
    file_name: str
    file_type: str

class RepairMultiFileRequest(BaseModel):
    file_list: list[RepairFileRequest]

class RepairFileDataResponse(BaseModel):
    original_name: str
    signed_url: str
    public_url: str

class RepairimgResponse(BaseModel):
    data: list[RepairFileDataResponse]

# ======================
# Create Repair
# ======================
class RepairRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    brand: str
    problem: str
    address_id: str
    img_url: str

class RepairInDB(BaseModel):
    user_id: str
    brand: str
    problem: str
    address_id: str
    img_url: str
    status: str = StatusRepair.PENDING_VERIFICATION
    created_at: datetime
    is_revoke: bool = False

# ======================
# Response Address Repair
# ======================
class ResponseAddressRepairDataResponse(BaseModel):
    id: str
    name: str
    tel: str
    address: str
    address_detail: str
    is_default: bool

class ResponseAddressRepairResponse(BaseModel):
    data: Optional[ResponseAddressRepairDataResponse] = None

# ======================
# Response Repair
# ======================
class RepairDataResponse(BaseModel):
    id: str
    brand: str
    problem: str
    img_url: Optional[str] = None
    status: str
    created_at: datetime
    price: Optional[str] = None

    name: Optional[str] = None
    tel: Optional[str] = None
    address: Optional[str] = None
    address_detail: Optional[str] = None

class RepairResponse(BaseModel):
    data: Optional[List[RepairDataResponse]] = None

# ======================
# Cancel Repair
# ======================
class CancelRepair(BaseModel):
    id: str
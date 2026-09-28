from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# ======================
# สร้างที่อยู่
# ======================
class AddressRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    name: str
    tel: str
    address: str
    address_detail: str

class AddressInDB(BaseModel):
    user_id: str
    name: str
    tel: str
    address: str
    address_detail: str
    created_at: datetime
    is_revoke: bool = False
    is_default: bool

# ======================
# แสดงผลที่อยู่
# ======================
class AddressDataResponse(BaseModel):
    id: str
    name: str
    tel: str
    address: str
    address_detail: str
    is_default: bool

class AddressResponse(BaseModel):
    data: Optional[list[AddressDataResponse]] = None

# ======================
# แสดงผลการแก้ไขที่อยู่
# ======================
class EditAddressResponseDataResponse(BaseModel):
    name: str
    tel: str
    address: str
    address_detail: str
    is_default: bool

class EditAddressResponseResponse(BaseModel):
    data: EditAddressResponseDataResponse

# ======================
# แสดงผลการลบที่อยู่
# ======================
class DeleteAddressResponseDataResponse(BaseModel):
    name: str
    tel: str
    address: str
    address_detail: str

class DeleteAddressResponseResponse(BaseModel):
    data: DeleteAddressResponseDataResponse

# ======================
# แก้ไขที่อยู่
# ======================
class EditAddressRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    name: Optional[str] = None
    tel: Optional[str] = None
    address: Optional[str] = None
    address_detail: Optional[str] = None
    is_default: Optional[bool] = None

# ======================
# บันทึกประวัติการแก้ไขที่อยู่
# ======================
class AddressHistoryInDB(BaseModel):
    user_id: str
    name: str
    tel: str
    address: str
    address_detail: str
    created_at: datetime
    is_revoke: bool = True
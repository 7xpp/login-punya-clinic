from types import SimpleNamespace
from config.config import supabase
from fastapi import HTTPException
from crud.unitofwork import UnitOfWork
from schemas.repair import RepairInDB, RepairFileDataResponse
from datetime import datetime, timezone
from schemas.status import StatusRepair
import uuid

class ServiceRepair:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Upload Repair Image
# ======================
    def service_repair_img(self, img_input, current_user):
        
        with self.uow as uow:

            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")

            data_img = []

            for item in img_input.file_list:

                allow_type = ["image/jpeg", "image/webp", "image/png"]
                if item.file_type not in allow_type:
                    raise HTTPException(status_code=400, detail="รองรับเฉพาะไฟล์ jpeg, png, webp")

                file_pull = item.file_name.split(".")[-1]
                file_name = f"{uuid.uuid4()}.{file_pull}"
                file_path = f"{filter_user.user_id}/{file_name}"

                try:
                    signed_url = supabase.storage.from_("img_SOCKET").create_signed_upload_url(file_path)
                    public_url = supabase.storage.from_("img_SOCKET").get_public_url(file_path)

                    img_obj=RepairFileDataResponse(
                        original_name=item.file_name,
                        signed_url=signed_url["signed_url"],
                        public_url=public_url
                    )
                    data_img.append(img_obj)

                except HTTPException:
                    uow.rollback()
                    raise
                except Exception as e:
                    uow.rollback()
                    raise HTTPException(status_code=400, detail=f"เกิดข้อผิดพลาดกับไฟล์ {item.file_name} {e}")

            return data_img

# ======================
# Response Address Repair
# ======================
    def service_response_address_repair(self, current_user):
        
        with self.uow as uow:

            filter_user = uow.address.get_by_user_default_address(str(current_user.user_id))
            
            if not filter_user:
                filter_user = uow.address.get_by_other_address(str(current_user.user_id))

            if not filter_user:
                return None

            return {
                "id": str(filter_user.id),
                "name": filter_user.name,
                "tel": filter_user.tel,
                "address": filter_user.address,
                "address_detail": filter_user.address_detail,
                "is_default": filter_user.is_default
            }


# ======================
# Create Repair
# ======================
    def service_repair(self, user_input, current_user):

        if not user_input.brand.strip() or not user_input.problem.strip() or not user_input.address_id.strip() or not user_input.img_url.strip():
            raise HTTPException(status_code=400, detail="กรุณากรอกข้อมูลให้ครบถ้วน")
        
        with self.uow as uow:

            filter_user = uow.address.get_by_user_id_and_address_id(str(current_user.user_id), str(user_input.address_id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูลที่อยู่")

            data_in_db = RepairInDB(
                user_id=str(current_user.user_id),
                brand=user_input.brand,
                problem=user_input.problem,
                address_id=user_input.address_id,
                img_url=user_input.img_url,
                status=StatusRepair.PENDING_VERIFICATION,
                created_at=datetime.now(timezone.utc),
                is_revoke=False
            )

            try:
                uow.repair.create(obj_in=data_in_db)
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการส่งซ่อม")

# ======================
# Cancel Repair
# ======================
    def service_cancel_repair(self, id, current_user):

        with self.uow as uow:

            filter_user = uow.repair.get_by_user_id_and_address_id(str(current_user.user_id), str(id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูลรายการซ่อม")

            try:
                uow.repair.update(
                    db_obj=filter_user,
                    obj_in={ "status": StatusRepair.CANCELLED}
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการส่งซ่อม")

# ======================
# Response Repair
# ======================
    def service_repair_response(self, current_user):

        with self.uow as uow:

            filter_user = uow.repair.get_by_user_id(str(current_user.user_id))
            
            if not filter_user:
                return []

            response = []

            for repairdata in filter_user:

                filter_address = uow.address.get_by_address_id(str(repairdata.address_id))

                response.append({
                    "id": str(repairdata.id),
                    "brand": repairdata.brand,
                    "problem": repairdata.problem,
                    "img_url": repairdata.img_url or "",
                    "status": repairdata.status,
                    "created_at": repairdata.created_at,
                    "price": f"{repairdata.price} บาท" if repairdata.price else "",
                    "name": filter_address.name if filter_address else "",
                    "tel": filter_address.tel if filter_address else "",
                    "address": filter_address.address if filter_address else "",
                    "address_detail": filter_address.address_detail if filter_address else ""
                })

            return response
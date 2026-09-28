from fastapi import HTTPException
from crud.unitofwork import UnitOfWork
from schemas.address import AddressInDB, AddressHistoryInDB
from datetime import datetime, timezone
import uuid

class ServiceAdress:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Create Address
# ======================
    def service_address(self, user_input, current_user):

        if not user_input.address.strip() or not user_input.address_detail.strip() or not user_input.name.strip() or not user_input.tel.strip():
            raise HTTPException(status_code=400, detail="กรุณากรอกข้อมูลให้ครบถ้วน")
            
        with self.uow as uow:

            filter_address = uow.address.get_by_count_user_id(str(current_user.user_id))

            if_first_address = (filter_address == 0)

            if filter_address >= 5:
                raise HTTPException(status_code=400, detail="คุณมีที่อยู่ได้สูงสุด 5 ที่อยู่")

            data_in_db = AddressInDB(
                user_id = str(current_user.user_id),
                name = user_input.name.strip(),
                tel = user_input.tel.strip(),
                address = user_input.address.strip(),
                address_detail = user_input.address_detail.strip(),
                created_at = datetime.now(timezone.utc),
                is_revoke = False,
                is_default = if_first_address
            )

            try:
                uow.address.create(obj_in=data_in_db)
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเพิ่มที่อยู่")

# ======================
# Address Response
# ======================
    def service_address_detail(self, current_user):

        with self.uow as uow:

            filter_user = uow.address.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                return []

            return [{
                "id": str(addressdata.id),
                "name": addressdata.name,
                "tel": addressdata.tel,
                "address": addressdata.address,
                "address_detail": addressdata.address_detail,
                "is_default": addressdata.is_default
            }
            for addressdata in filter_user
        ]

# ======================
# Edit Address Response
# ======================
    def service_edit_address_response(self,current_user, id):

        with self.uow as uow:

            filter_user = uow.address.get_by_user_id_and_address_id(str(current_user.user_id), id)

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")

            return {
                "name": filter_user.name,
                "tel": filter_user.tel,
                "address": filter_user.address,
                "address_detail": filter_user.address_detail,
                "is_default": filter_user.is_default
            }

# ======================
# Edit Address
# ======================
    def service_edit_address(self, user_input, current_user, id):

        update_user = user_input.model_dump(exclude_unset=True)

        if not update_user:
            raise HTTPException(status_code=400, detail="กรุณากรอกข้อมูลให้ครบถ้วน")

        with self.uow as uow:

            filter_user = uow.address.get_by_user_id_and_address_id(str(current_user.user_id), id)
            filter_user_list = uow.address.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")

            data_in_db = AddressHistoryInDB(
                user_id = str(current_user.user_id),
                name = filter_user.name,
                tel = filter_user.tel,
                address = filter_user.address,
                address_detail = filter_user.address_detail,
                created_at = datetime.now(timezone.utc),
                is_revoke = True
            )

            try:
                if update_user.get("is_default") is True:
                    for item in filter_user_list:
                        uow.address.update(db_obj=item, obj_in={"is_default": False})
                        
                uow.address.update(
                    db_obj=filter_user,
                    obj_in={"update_at": datetime.now(timezone.utc), **update_user}
                )
                uow.addresshis.create(obj_in=data_in_db)
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเปลี่ยนข้อมูล")

# ======================
# Delete Address Response
# ======================

    def service_delete_address_response(self, current_user, id):

        with self.uow as uow:

            filter_user = uow.address.get_by_user_id_and_address_id(str(current_user.user_id), id)

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")
            
            return {
                "name": filter_user.name,
                "tel": filter_user.tel,
                "address": filter_user.address,
                "address_detail": filter_user.address_detail
            }

# ======================
# Delete Address
# ======================
    def service_delete_address(self, current_user, id):

        with self.uow as uow:

            filter_user = uow.address.get_by_user_id_and_address_id(str(current_user.user_id), id)


            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")

            filter_default_address = filter_user.is_default

            data_in_db = AddressHistoryInDB(
                user_id = str(current_user.user_id),
                name = filter_user.name,
                tel = filter_user.tel,
                address = filter_user.address,
                address_detail = filter_user.address_detail,
                created_at = datetime.now(timezone.utc),
                is_revoke = True
            )

            try:
                uow.address.remove(id=filter_user.id)
                uow.addresshis.create(obj_in=data_in_db)

                if filter_default_address:
                    filter_other_user = uow.address.get_by_other_address(filter_user.user_id)
                    if filter_other_user:
                        uow.address.update(db_obj=filter_other_user, obj_in={"is_default": True})
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception as e:
                uow.rollback()
                raise HTTPException(status_code=400, detail=f"เกิดข้อผิดพลาดในการลบข้อมูล: {e}")
from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud.unitofwork import UnitOfWork


class ServiceUserDetail:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Edit Detail
# ======================
    def service_edit_user_detail(self, user_input, current_user):

        with self.uow as uow:

            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))
            filter_username = uow.userdetail.get_by_username(user_input.username)

            if not filter_user:
                return HTTPException(status_code=400, detail="ไม่พบผู้ใช้")
            if filter_username:
                return HTTPException(status_code=400, detail="ชื่อผู้ใช้งานนี้มีผู้ใช้งานแล้ว")


            try:
                uow.auth.update(
                    db_obj=filter_user,
                    obj_in=user_input.username
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเปลี่ยนข้อมูล")

# ======================
# Res Detail
# ======================
    def userdetail(self, current_user):

        with self.uow as uow:
            
            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")

            return {
                "username": filter_user.username,
                "email": filter_user.email,
                "tel": filter_user.tel,
            }
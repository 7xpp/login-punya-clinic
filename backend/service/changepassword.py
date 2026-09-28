from fastapi import HTTPException
from security.verifypassword import verify_password
from crud.unitofwork import UnitOfWork
from security.hashpassword import hash_password
from datetime import datetime, timezone
from schemas.changepassword import ChangePasswordInDB
from security.token.changepassword import create_change_password_token


class ServiceChangePassword:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Check Password
# ======================
    def service_changepassword(self, user_input, current_user, response):

        with self.uow as uow:

            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")
            if not verify_password(user_input.password, filter_user.password):
                raise HTTPException(status_code=400, detail="รหัสผ่านไม่ถูกต้อง")

            change_password_token, change_password_token_exp = create_change_password_token(str(current_user.user_id))

            response.set_cookie(
                key="change_password_token",
                value=change_password_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=600,
                path="/"
            )

            data_in_db = ChangePasswordInDB(
                user_id=str(current_user.user_id),
                change_password_token=change_password_token,
                change_password_token_exp=change_password_token_exp,
                change_password_token_is_revoked=False,
                created_at=datetime.now(timezone.utc),
                is_revoked=False
            )

            try:
                uow.changepassword.create(obj_in=data_in_db)
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการส่งคำขอ")

# ======================
# Confirm Password
# ======================
    def service_confirm_changepassword(self, user_input, current_user):

        if user_input.password != user_input.confirmpassword:
            raise HTTPException(status_code=400, detail="รหัสผ่านใหม่ไม่ตรงกัน")

        hashed_password = hash_password(user_input.password)

        with self.uow as uow:

            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))
            filter_changepassword = uow.changepassword.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")
            if not filter_changepassword:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")
            if filter_changepassword.change_password_token_is_revoked is True:
                raise HTTPException(status_code=400, detail="โทเค็นถูกยกเลิกแล้ว")
            if filter_changepassword.is_revoked is True:
                raise HTTPException(status_code=400, detail="ถูกเพิกถอนแล้ว")

            try:
                uow.changepassword.update(
                    db_obj=filter_changepassword,
                    obj_in={
                        "change_password_token": None,
                        "change_password_token_exp": None,
                        "change_password_token_is_revoked": True,
                        "updated_at": datetime.now(timezone.utc),
                        "is_revoked": True
                    }
                )
                uow.auth.update(
                    db_obj=filter_user,
                    obj_in={
                        "password": hashed_password
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเปลี่ยนรหัสผ่าน")
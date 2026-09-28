from crud.unitofwork import UnitOfWork
from fastapi import HTTPException
from security.token.jwt import create_access_token, create_refresh_token
from security.verifypassword import verify_password
from security.hashpassword import hash_password
from schemas.auth import SignupInDB
from datetime import datetime, timezone
import uuid

class ServiceAuth:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Signup
# ======================
    def service_signup(self, user_input):

        with self.uow as uow:

            filter_username = uow.auth.get_by_username(user_input.username)
            filter_email = uow.auth.get_by_email(user_input.email)
            filter_tel = uow.auth.get_by_tel(user_input.tel)

            if filter_username:
                raise HTTPException(status_code=400, detail="ชื่อผู้ใช้งานนี้มีผู้ใช้งานแล้ว")
            if filter_email:
                raise HTTPException(status_code=400, detail="อีเมลนี้มีผู้ใช้งานแล้ว")
            if filter_tel:
                raise HTTPException(status_code=400, detail="เบอร์โทรศัพท์นี้มีผู้ใช้งานแล้ว")

            hashed_password = hash_password(user_input.password)

            data_in_db = SignupInDB(
                user_id=str(uuid.uuid4()),
                username=user_input.username,
                email=user_input.email,
                password=hashed_password,
                tel=user_input.tel,
                created_at=datetime.now(timezone.utc)
            )

            try:
                uow.auth.create(obj_in=data_in_db) 
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการสมัครสมาชิก")

# ======================
# Login
# ======================
    def service_login(self, user_input, response):

        with self.uow as uow:

            filter_login = uow.auth.get_by_email(user_input.email)

            if not filter_login:
                raise HTTPException(status_code=400, detail="อีเมลหรือรหัสผ่านไม่ถูกต้อง")
            if not verify_password(user_input.password, filter_login.password):
                raise HTTPException(status_code=400, detail="อีเมลหรือรหัสผ่านไม่ถูกต้อง")
                
            access_token, access_token_exp = create_access_token(filter_login.user_id)
            refresh_token, refresh_token_exp = create_refresh_token(filter_login.user_id)

            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=900,
                path="/"
            )
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=60*60*24*7,
                path="/"
            )
            
            try:
                uow.auth.update(
                    db_obj=filter_login,
                    obj_in={
                        "refresh_token": refresh_token,
                        "refresh_token_exp": refresh_token_exp,
                        "updated_at": datetime.now(timezone.utc),
                        "is_revoked": False
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเข้าสู่ระบบ")

# ======================
# Logout
# ======================
    def service_logout(self, current_user, response):

        response.delete_cookie(key="access_token", path="/")
        response.delete_cookie(key="refresh_token", path="/")

        with self.uow as uow:
            try:
                uow.auth.update(
                    db_obj=current_user,
                    obj_in={
                        "refresh_token": None,
                        "refresh_token_exp": None,
                        "is_revoked": True
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการออกจากระบบ")

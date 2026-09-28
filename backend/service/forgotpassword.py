from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
import random
from security.hashpassword import hash_password
from crud.unitofwork import UnitOfWork
from security.token.forgot_password_jwt import create_reset_password_otp_token, create_reset_password_token
from schemas.forgotpassword import ForgotPasswordOTPInDB

class ServiceFCC:
    def __init__(self, uow: UnitOfWork  ):
        self.uow = uow

# ======================
# Forgot Password
# ======================
    def service_forgotpassword(self, current_user, response):

        with self.uow as uow:

            otp_code = str(random.randint(100000, 999999))
            otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

            reset_password_otp_token, reset_password_otp_token_exp = create_reset_password_otp_token(str(current_user.user_id))

            response.set_cookie(
                key="reset_password_otp_token",
                value=reset_password_otp_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=600,
                path="/"
            )

            data_in_db = ForgotPasswordOTPInDB(
                user_id = str(current_user.user_id),
                otp = otp_code,
                otp_exp = otp_exp,
                otp_is_revoked = False,
                reset_password_otp_token = reset_password_otp_token,
                reset_password_otp_token_exp = reset_password_otp_token_exp,
                reset_password_otp_is_revoked = False,
                created_at = datetime.now(timezone.utc),
                is_revoked = False
            )

            try:
                uow.forgotpassword.create(obj_in=data_in_db)
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการสร้าง OTP")

# ======================
# Create OTP Again
# ======================
    def service_create_otp_again(self, current_user, response):
         
        otp = str(random.randint(100000, 999999))
        otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

        reset_password_otp_token, reset_password_otp_token_exp = create_reset_password_otp_token(str(current_user.user_id))

        response.set_cookie(
            key="reset_password_otp_token",
            value=reset_password_otp_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=600,
            path="/"
        )

        with self.uow as uow:

            filter_user = uow.forgotpassword.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")

            try:
                uow.forgotpassword.update(
                    db_obj=filter_user,
                    obj_in={
                        "otp": otp,
                        "otp_exp": otp_exp,
                        "otp_is_revoked": False,
                        "reset_password_otp_token": reset_password_otp_token,
                        "reset_password_otp_token_exp": reset_password_otp_token_exp,
                        "reset_password_otp_is_revoked": False,
                        "is_revoked" : False
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการสร้าง OTP")

# ======================
# Check OTP
# ======================
    def service_checkotp(self, user_input, current_user, response):

        with self.uow as uow:

            filter_user = uow.forgotpassword.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")
            if str(user_input.otp) != str(filter_user.otp):
                raise HTTPException(status_code=400, detail="รหัส OTP ไม่ถูกต้อง")
            if filter_user.reset_password_otp_is_revoked is True:
                raise HTTPException(status_code=400, detail="โทเค็นถูกยกเลิกแล้ว")
            if filter_user.otp_is_revoked is True:
                raise HTTPException(status_code=400, detail="OTP ถูกยกเลิกแล้ว")

            otp_exp = filter_user.otp_exp

            if otp_exp:
                if otp_exp.tzinfo is None:
                    otp_exp = otp_exp.replace(tzinfo=timezone.utc)
                if otp_exp < datetime.now(timezone.utc):
                    raise HTTPException(status_code=400, detail="รหัส OTP หมดอายุแล้ว")

            reset_password_token, reset_password_token_exp = create_reset_password_token(str(current_user.user_id))

            response.set_cookie(
                key="reset_password_token",
                value=reset_password_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=600,
                path="/"
            )

            try:
                uow.forgotpassword.update(
                    db_obj=filter_user,
                    obj_in={
                        "reset_password_token": reset_password_token,
                        "reset_password_token_exp": reset_password_token_exp,
                        "reset_password_token_is_revoked": False,

                        "reset_password_otp_token": None,
                        "reset_password_otp_token_exp": None,
                        "reset_password_otp_is_revoked": True,

                        "otp": None,
                        "otp_exp": None,
                        "otp_is_revoked": True
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการยืนยัน OTP")

# ======================
# Confirm Password
# ======================
    def service_confirmpassword(self, user_input, current_user):

        if user_input.password != user_input.confirmpassword:
            raise HTTPException(status_code=400, detail="รหัสผ่านใหม่ไม่ตรงกัน")

        hashed_password = hash_password(user_input.password)

        with self.uow as uow:

            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))
            filter_user_forgot_password = uow.forgotpassword.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")
            if not filter_user_forgot_password:
                raise HTTPException(status_code=404, detail="ไม่พบข้อมูล")
            if filter_user_forgot_password.reset_password_token_is_revoked is True:
                raise HTTPException(status_code=400, detail="โทเค็นถูกยกเลิกแล้ว")

            try:
                uow.auth.update(
                    db_obj=filter_user,
                    obj_in={
                        "password": hashed_password,
                    }
                )
                uow.forgotpassword.update(
                    db_obj=filter_user_forgot_password,
                    obj_in={
                        "reset_password_token": None,
                        "reset_password_token_exp": None,
                        "reset_password_token_is_revoked": True,
                        "is_revoked": True,
                        "updated_at": datetime.now(timezone.utc)
                        }
                    )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการเปลี่ยนรหัสผ่าน")
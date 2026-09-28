from crud.unitofwork import UnitOfWork
from fastapi import HTTPException
from security.verifypassword import verify_password
import random
from security.token.reset_email_jwt import create_reset_email_otp_token, create_reset_email_token
from datetime import datetime, timedelta, timezone
from schemas.reset_email import ResetEmailCheckOTPInDB

class ServiceResetEmail:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
# ======================
# Create OTP
# ======================
    def service_reset_email(self, user_input, current_user, response):

        with self.uow as uow:

            filter_user = uow.auth.get_by_email(user_input.email)
            filter_password = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not verify_password(user_input.password, filter_password.password):
                raise HTTPException(status_code=400, detail="รหัสผ่านไม่ถูกต้อง")
            if filter_user:
                raise HTTPException(status_code=400, detail="อีเมลนี้มีผู้ใช้งานแล้ว")

            otp = str(random.randint(100000, 999999))
            otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

            reset_email_otp_token, reset_email_otp_token_exp = create_reset_email_otp_token(str(current_user.user_id))

            response.set_cookie(
                key="reset_email_otp_token",
                value=reset_email_otp_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=600,
                path="/"
            )

            data_in_db = ResetEmailCheckOTPInDB(
                user_id = str(current_user.user_id),
                otp = otp,
                otp_exp = otp_exp,
                otp_is_revoked = False,
                reset_email_otp_token = reset_email_otp_token,
                reset_email_otp_token_exp = reset_email_otp_token_exp,
                reset_email_otp_is_revoked = False,
                created_at = datetime.now(timezone.utc),
                email = user_input.email,
                is_revoke = False
            )

            with self.uow as uow:
                try:
                    uow.reset_email.create(obj_in=data_in_db)
                    uow.commit()
                except HTTPException:
                    uow.rollback()
                    raise
                except Exception:
                    uow.rollback()
                    raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการสร้าง OTP")

# ======================
# Create OTP again
# ======================
    def service_create_otp_again(self, current_user, response):

        otp = str(random.randint(100000, 999999))
        otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

        reset_email_otp_token, reset_email_otp_token_exp = create_reset_email_otp_token(str(current_user.user_id))

        response.set_cookie(
            key="reset_email_otp_token",
            value=reset_email_otp_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=600,
            path="/"
        )

        with self.uow as uow:

            filter_user = uow.reset_email.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")

            try:
                uow.reset_email.update(
                    db_obj=filter_user,
                    obj_in={
                        "otp": otp,
                        "otp_exp": otp_exp,
                        "otp_is_revoked": False,
                        "reset_email_otp_token": reset_email_otp_token,
                        "reset_email_otp_token_exp": reset_email_otp_token_exp,
                        "reset_email_otp_is_revoked": False,
                        "is_revoke": False
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
    def service_check_otp(self, user_input, current_user, response):

        with self.uow as uow:

            filter_user_data = uow.reset_email.get_by_user_id(str(current_user.user_id))
            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not filter_user_data:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")
            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบผู้ใช้")
            if str(user_input.otp) != str(filter_user_data.otp):
                raise HTTPException(status_code=400, detail="รหัส OTP ไม่ถูกต้อง")
            if filter_user_data.reset_email_otp_is_revoked is True:
                raise HTTPException(status_code=400, detail="โทเค็นถูกยกเลิกแล้ว")
            if filter_user_data.otp_is_revoked is True:
                raise HTTPException(status_code=400, detail="OTP ถูกยกเลิกแล้ว")

            otp_exp = filter_user_data.otp_exp

            if otp_exp:
                if otp_exp.tzinfo is None:
                    otp_exp = otp_exp.replace(tzinfo=timezone.utc)
                if otp_exp < datetime.now(timezone.utc):
                    raise HTTPException(status_code=400, detail="รหัส OTP หมดอายุแล้ว")

            try:
                uow.reset_email.update(
                    db_obj=filter_user_data,
                    obj_in={
                        "reset_email_otp_token": None,
                        "reset_email_otp_token_exp": None,
                        "reset_email_otp_is_revoked": True,
                        "otp": None,
                        "otp_exp": None,
                        "otp_is_revoked": True,
                        "is_revoked": True,
                        "updated_at": datetime.now(timezone.utc)
                    }
                )
                uow.auth.update(
                    db_obj=filter_user,
                    obj_in={
                        "email": filter_user_data.email
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการยืนยัน OTP")
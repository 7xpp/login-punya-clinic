from schemas.resettel import ResetTelCheckOTPInDB
from security.token.resettel import create_reset_tel_otp_token, create_reset_tel_token
from datetime import timedelta, datetime, timezone
import random
from fastapi import HTTPException
from security.verifypassword import verify_password
from crud.unitofwork import UnitOfWork

class ServiceResetTel:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

# ======================
# Create OTP
# ======================
    def service_reset_tel(self, user_input, current_user, response):

        with self.uow as uow:

            filter_user = uow.auth.get_by_tel(user_input.tel)
            filter_password = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not verify_password(user_input.password, filter_password.password):
                raise HTTPException(status_code=400, detail="รหัสผ่านไม่ถูกต้อง")
            if filter_user:
                raise HTTPException(status_code=400, detail="เบอร์โทรนี้มีผู้ใช้งานแล้ว")

            otp = str(random.randint(100000, 999999))
            otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

            reset_tel_otp_token, reset_tel_otp_token_exp = create_reset_tel_otp_token(str(current_user.user_id))

            response.set_cookie(
                key="reset_tel_otp_token",
                value=reset_tel_otp_token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=600,
                path="/"
            )

            data_in_db = ResetTelCheckOTPInDB(
                user_id = str(current_user.user_id),
                otp = otp,
                otp_exp = otp_exp,
                otp_is_revoked = False,
                reset_tel_otp_token = reset_tel_otp_token,
                reset_tel_otp_token_exp = reset_tel_otp_token_exp,
                reset_tel_otp_is_revoked = False,
                created_at = datetime.now(timezone.utc),
                tel = user_input.tel,
                is_revoke = False
            )

            with self.uow as uow:
                try:
                    uow.reset_tel.create(obj_in=data_in_db)
                    uow.commit()
                except HTTPException:
                    uow.rollback()
                    raise
                except Exception as e:
                    uow.rollback()
                    raise HTTPException(status_code=400, detail=f"เกิดข้อผิดพลาดในการสร้าง OTP: {e}")

# ======================
# Create OTP again
# ======================
    def service_create_otp_again(self, current_user, response):

        otp = str(random.randint(100000, 999999))
        otp_exp = datetime.now(timezone.utc) + timedelta(minutes=5)

        reset_tel_otp_token, reset_tel_otp_token_exp = create_reset_tel_otp_token(str(current_user.user_id))

        response.set_cookie(
            key="reset_tel_otp_token",
            value=reset_tel_otp_token,
            httponly=True,
            secure=False,
            samesite="lax",
            max_age=600,
            path="/"
        )

        with self.uow as uow:

            filter_user = uow.reset_tel.get_by_user_id(str(current_user.user_id))

            if not filter_user:
                raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้")

            try:
                uow.reset_tel.update(
                    db_obj=filter_user,
                    obj_in={
                        "otp": otp,
                        "otp_exp": otp_exp,
                        "otp_is_revoked": False,
                        "reset_tel_otp_token": reset_tel_otp_token,
                        "reset_tel_otp_token_exp": reset_tel_otp_token_exp,
                        "reset_tel_otp_is_revoked": False,
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

            filter_user_data = uow.reset_tel.get_by_user_id(str(current_user.user_id))
            filter_user = uow.current_user.get_by_user_id(str(current_user.user_id))

            if not filter_user_data:
                raise HTTPException(status_code=400, detail="ไม่พบข้อมูล")
            if not filter_user:
                raise HTTPException(status_code=400, detail="ไม่พบผู้ใช้")
            if str(user_input.otp) != str(filter_user_data.otp):
                raise HTTPException(status_code=400, detail="รหัส OTP ไม่ถูกต้อง")
            if filter_user_data.reset_tel_otp_is_revoked is True:
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
                uow.reset_tel.update(
                    db_obj=filter_user_data,
                    obj_in={
                        "reset_tel_otp_token": None,
                        "reset_tel_otp_token_exp": None,
                        "reset_tel_otp_is_revoked": True,
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
                        "tel": filter_user_data.tel
                    }
                )
                uow.commit()
            except HTTPException:
                uow.rollback()
                raise
            except Exception:
                uow.rollback()
                raise HTTPException(status_code=400, detail="เกิดข้อผิดพลาดในการยืนยัน OTP")
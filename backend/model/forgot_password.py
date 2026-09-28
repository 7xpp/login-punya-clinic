from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, UUID, ForeignKey, Boolean
from database.database import Base
import uuid


class OLDForgotPassword(Base):
    __tablename__ = "forgotpassword"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=False)

    reset_password_otp_token = Column(String, nullable=True)
    reset_password_otp_token_exp = Column(DateTime, nullable=True)
    reset_password_otp_is_revoked = Column(Boolean, default=False, nullable=True)

    reset_password_token = Column(String, nullable=True)
    reset_password_token_exp = Column(DateTime, nullable=True)
    reset_password_token_is_revoked = Column(Boolean, default=False, nullable=True)

    otp = Column(String, nullable=True)
    otp_exp = Column(DateTime, nullable=True)
    otp_is_revoked = Column(Boolean, default=False, nullable=True)

    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=True)

    is_revoked = Column(Boolean, default=False, nullable=False)
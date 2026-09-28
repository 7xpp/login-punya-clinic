from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, UUID, ForeignKey, Boolean
from database.database import Base
import uuid

class OLDResetEmail(Base):
    __tablename__ = "reset_email"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=False)

    reset_email_otp_token = Column(String, nullable=True)
    reset_email_otp_token_exp = Column(DateTime, nullable=True)
    reset_email_otp_is_revoked = Column(Boolean, default=False)
    
    otp = Column(String, nullable=True)
    otp_exp = Column(DateTime, nullable=True)
    otp_is_revoked = Column(Boolean, default=False, nullable=False)

    email = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=True)

    is_revoked = Column(Boolean, default=False, nullable=False)
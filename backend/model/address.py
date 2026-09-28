from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, UUID, Boolean
from database.database import Base
import uuid

class OLDAddress(Base):
    __tablename__ = "address"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=False)

    name = Column(String, nullable=False)
    tel = Column(String, nullable=False)
    address = Column(String, nullable=False)
    address_detail = Column(String, nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=True)

    is_revoke = Column(Boolean, default=False, nullable=True)

    is_default = Column(Boolean, default=False, nullable=True)
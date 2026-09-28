from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, UUID, ForeignKey, Boolean
from database.database import Base
import uuid

class OLDAddressHistory(Base):
    __tablename__ = "addresshistory"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=False)

    name = Column(String, nullable=False)
    tel = Column(String, nullable=False)
    address = Column(String, nullable=False)
    address_detail = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    is_revoke = Column(Boolean, default=False, nullable=True)
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String, UUID, ForeignKey, Boolean
from database.database import Base
import uuid


class OLDRepair(Base):
    __tablename__ = "repair"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=False)

    brand = Column(String, nullable=False)
    problem = Column(String, nullable=False)
    address_id = Column(UUID, nullable=False)
    img_url = Column(String, nullable=True)
    status = Column(String, nullable=False)
    price = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=True)

    is_revoke = Column(Boolean, default=False)
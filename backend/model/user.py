from sqlalchemy import Column, DateTime, String, UUID, ForeignKey, Boolean
from database.database import Base
import uuid
from datetime import datetime, timezone


class OLDUser(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID, default=uuid.uuid4, nullable=True)

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    tel = Column(String, unique=True, nullable=False)

    refresh_token = Column(String, nullable=True)
    refresh_token_exp = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=True)

    is_revoked = Column(Boolean, default=False, nullable=True)
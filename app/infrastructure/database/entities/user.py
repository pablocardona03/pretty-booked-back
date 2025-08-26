import uuid

from sqlalchemy import Column, String, DateTime, func

from app.infrastructure.database.config import Base
from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database.mixins import TimestampMixin


class UserEntity(Base, TimestampMixin):
    __tablename__ = 'users'
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    business_name = Column(String, nullable=False)
    cell_phone = Column(String(30), nullable=False)
    description = Column(String, nullable=False)
    address = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

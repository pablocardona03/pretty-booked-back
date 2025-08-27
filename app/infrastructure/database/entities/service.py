import uuid
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.domain.enums import ServiceCategory, ServiceTechnique
from app.infrastructure.database.config import Base
from app.infrastructure.database.mixins import TimestampMixin, IsActiveMixin


class ServiceEntity(Base, TimestampMixin, IsActiveMixin):
    __tablename__ = 'services'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    description = Column(String, nullable=True)
    category = Column(ENUM(ServiceCategory, name="service_category"), nullable=True)
    technique = Column(ENUM(ServiceTechnique, name="service_technique"), nullable=True)
    price = Column(Float, nullable=True)
    duration = Column(Float, nullable=True)
    owner_id = Column(UUID, ForeignKey('users.id', ondelete="CASCADE"), nullable=True, index=True)

    owner = relationship("UserEntity", back_populates="services")
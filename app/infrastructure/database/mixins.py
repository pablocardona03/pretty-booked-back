import datetime
from sqlalchemy import Column, DateTime, func, Boolean
from sqlalchemy.orm import declarative_mixin

@declarative_mixin
class TimestampMixin:
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

class IsActiveMixin:
    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

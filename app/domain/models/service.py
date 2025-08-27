from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

@dataclass
class ServiceModel:
    description: str
    category: str
    technique: str
    price: float
    duration: int
    owner_id: UUID

    is_active: Optional[bool] = True
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

@dataclass
class UserModel:
    name: str
    last_name: str
    email: str
    password: str
    business_name: str
    cell_phone: str
    description: str
    address: str

    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

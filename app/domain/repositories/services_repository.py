from abc import ABC
from uuid import UUID

from app.domain.models.service import ServiceModel
from app.domain.repositories.base_repository import BaseRepository

class ServicesRepository(BaseRepository[ServiceModel, UUID], ABC):
    pass
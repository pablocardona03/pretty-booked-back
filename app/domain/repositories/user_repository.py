from abc import ABC
from uuid import UUID
from app.domain.models.user import UserModel
from app.domain.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[UserModel, UUID], ABC):
    pass
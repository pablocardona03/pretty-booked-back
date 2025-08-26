from typing import Optional
from uuid import UUID

from sqlalchemy import select
from app.domain.models.user import UserModel
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.entities import UserEntity
from app.infrastructure.database.repositories.base_sqlalchemy_repository import BaseSqlAlchemyRepository
from app.infrastructure.database.mappers.user_mapper import entity_to_model, model_to_new_entity

class UserSqlAlchemyRepository(UserRepository, BaseSqlAlchemyRepository):
    def get_by_id(self, user_id: UUID) -> Optional[UserModel]:
        entity = self.db_session.execute(
            select(UserEntity).where(UserEntity.id == user_id)
        ).scalar_one_or_none()
        return entity_to_model(entity) if entity else None

    def get_all(self) -> list[UserModel]:
        entities = self.db_session.execute(select(UserEntity)).scalars().all()
        return [entity_to_model(e) for e in entities]

    def create(self, item: UserModel) -> UserModel:
        try:
            entity = model_to_new_entity(item)
            self.db_session.add(entity)
            self.db_session.flush()
            self.db_session.refresh(entity)
            self.db_session.commit()
            return entity_to_model(entity)
        except Exception:
            self.db_session.rollback()
            raise

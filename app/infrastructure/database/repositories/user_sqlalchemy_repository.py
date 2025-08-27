from typing import Optional
from uuid import UUID

from sqlalchemy import select
from app.domain.models.user import UserModel
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.entities import UserEntity
from app.infrastructure.database.repositories.base_sqlalchemy_repository import BaseSqlAlchemyRepository
from app.infrastructure.database.mappers.mapper import entity_to_model, model_to_new_entity, update_model_to_entity

class UserSqlAlchemyRepository(UserRepository, BaseSqlAlchemyRepository):

    def get_by_id(self, user_id: UUID) -> Optional[UserModel]:
        entity = self.db_session.execute(
            select(UserEntity).where(UserEntity.id == user_id)
        ).scalar_one_or_none()
        return entity_to_model(entity, UserModel) if entity else None

    def get_all(self) -> list[UserModel]:
        entities = self.db_session.execute(select(UserEntity)).scalars().all()
        return [entity_to_model(e, UserModel) for e in entities]

    def create(self, item: UserModel) -> UserModel:
        try:
            entity = model_to_new_entity(item, UserEntity)
            self.db_session.add(entity)
            self.db_session.commit()
            return entity_to_model(entity, UserModel)
        except Exception:
            self.db_session.rollback()
            raise

    def update(self, item: UserModel) -> UserModel:
        try:
            entity: Optional[UserEntity] = self.db_session.get(UserEntity, item.id)
            if not entity:
                raise Exception(f"User {item.id} not found")

            update_model_to_entity(entity, item)

            self.db_session.commit()
            return entity_to_model(entity, UserModel)
        except Exception:
            self.db_session.rollback()
            raise

    def delete(self, item: UserModel) -> None:
        pass

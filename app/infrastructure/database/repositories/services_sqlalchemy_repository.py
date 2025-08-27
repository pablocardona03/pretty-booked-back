from typing import Optional
from uuid import UUID

from sqlalchemy import select
from app.domain.models.service import ServiceModel
from app.domain.repositories.services_repository import ServicesRepository
from app.infrastructure.database.entities.service import ServiceEntity
from app.infrastructure.database.repositories.base_sqlalchemy_repository import BaseSqlAlchemyRepository
from app.infrastructure.database.mappers.mapper import entity_to_model, model_to_new_entity, update_model_to_entity

class ServicesSqlAlchemyRepository(ServicesRepository, BaseSqlAlchemyRepository):

    def get_by_id(self, service_id: UUID) -> Optional[ServiceModel]:
        entity = self.db_session.execute(
            select(ServiceEntity).where(ServiceEntity.id == service_id)
        ).scalar_one_or_none()
        return entity_to_model(entity, ServiceModel) if entity else None

    def get_all(self) -> list[ServiceModel]:
        entities = self.db_session.execute(select(ServiceEntity)).scalars().all()
        return [entity_to_model(e, ServiceModel) for e in entities]

    def create(self, item: ServiceModel) -> ServiceModel:
        try:
            entity = model_to_new_entity(item, ServiceEntity)
            self.db_session.add(entity)
            self.db_session.commit()
            return entity_to_model(entity, ServiceModel)
        except Exception:
            self.db_session.rollback()
            raise

    def update(self, item: ServiceModel) -> ServiceModel:
        try:
            entity: Optional[ServiceEntity] = self.db_session.get(ServiceEntity, item.id)
            if not entity:
                raise Exception(f"Service {item.id} not found")

            update_model_to_entity(entity, item)

            self.db_session.commit()
            return entity_to_model(entity, ServiceModel)
        except Exception:
            self.db_session.rollback()
            raise

    def delete(self, item: ServiceModel) -> None:
        pass
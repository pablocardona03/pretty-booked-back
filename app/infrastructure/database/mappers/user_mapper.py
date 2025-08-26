from app.domain.models.user import UserModel
from app.infrastructure.database.entities.user import UserEntity

def entity_to_model(entity: UserEntity) -> UserModel:
    return UserModel(
        id=entity.id,
        name=entity.name,
        last_name=entity.last_name,
        business_name=entity.business_name,
        cell_phone=entity.cell_phone,
        email=entity.email,
        description=entity.description,
        address=entity.address,
        created_at=entity.created_at,
        updated_at=getattr(entity, "updated_at", None),
    )

def model_to_new_entity(model: UserModel) -> UserEntity:
    return UserEntity(
        name=model.name,
        last_name=model.last_name,
        email=model.email,
        password=model.password,
        business_name=model.business_name,
        cell_phone=model.cell_phone,
        description=model.description,
        address=model.address,
    )

def update_model_to_entity(entity: UserEntity, model: UserModel) -> None:
    if model.name is not None: entity.name = model.name
    if model.last_name is not None: entity.last_name = model.last_name
    if model.email is not None: entity.email = model.email
    if model.password is not None: entity.password = model.password
    if model.business_name is not None: entity.business_name = model.business_name
    if model.cell_phone is not None: entity.cell_phone = model.cell_phone
    if model.description is not None: entity.description = model.description
    if model.address is not None: entity.address = model.address
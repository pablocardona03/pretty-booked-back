from typing import Type, TypeVar

ModelT = TypeVar("ModelT")
EntityT = TypeVar("EntityT")

def entity_to_model(entity: EntityT, model_class: Type[ModelT]) -> ModelT:
    entity_dict = vars(entity)
    return model_class(**entity_dict)

def model_to_new_entity(model: ModelT, entity_class: Type[EntityT]) -> EntityT:
    model_dict = vars(model)
    return entity_class(**model_dict)

def update_model_to_entity(entity: EntityT, model: ModelT) -> None:
    for key, value in vars(model).items():
        if value is not None and hasattr(entity, key):
            setattr(entity, key, value)

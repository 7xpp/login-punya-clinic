from typing import Generic, List, Optional, Type, TypeVar, Union, Dict, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CrudBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def create(self, obj_in) -> ModelType:
        if hasattr(obj_in, "model_dump"):
            create_data = obj_in.model_dump()
        elif hasattr(obj_in, "dict"):
            create_data = obj_in.dict()
        else:
            create_data = obj_in
        db_obj = self.model(**create_data)
        self.db.add(db_obj)
        self.db.flush()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True) if hasattr(obj_in, "model_dump") else obj_in.dict(exclude_unset=True)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])

        self.db.add(db_obj)
        self.db.flush()
        self.db.refresh(db_obj)
        return db_obj

    def remove(self, *, id: Any) -> Optional[ModelType]:
        obj = self.db.query(self.model).get(id)
        if obj:
            self.db.delete(obj)
            self.db.flush()
        return obj
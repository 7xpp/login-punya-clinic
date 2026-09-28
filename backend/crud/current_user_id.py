from model.user import OLDUser
from crud.base import CrudBase
from sqlalchemy.orm import Session

class CrudCurrentID(CrudBase[OLDUser]):
    def __init__(self, db: Session):
        super().__init__(model=OLDUser, db=db)
        self.db = db

    def get_by_user_id(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()
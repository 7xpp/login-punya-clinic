from sqlalchemy.orm import Session
from model.user import OLDUser
from crud.base import CrudBase

class CrudUserDetail(CrudBase[OLDUser]):
    def __init__(self, db: Session):
        super().__init__(model=OLDUser, db=db)
        self.db = db

    def get_by_username(self, username: str):
        return self.db.query(self.model).filter(self.model.username == username).first()
from model.user import OLDUser
from crud.base import CrudBase
from sqlalchemy.orm import Session

class CrudAuth(CrudBase[OLDUser]):
    def __init__(self, db: Session):
        super().__init__(model=OLDUser, db=db)
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_by_username(self, username: str):
        return self.db.query(self.model).filter(self.model.username == username).first()

    def get_by_tel(self, tel: str):
        return self.db.query(self.model).filter(self.model.tel == tel).first()
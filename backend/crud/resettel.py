from sqlalchemy.orm import Session
from model.resettel import OLDResetTel
from crud.base import CrudBase

class CrudResetTel(CrudBase[OLDResetTel]):
    def __init__(self, db: Session):
        super().__init__(model=OLDResetTel, db=db)
        self.db = db

    def get_by_user_id(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).order_by(self.model.created_at.desc()).first()
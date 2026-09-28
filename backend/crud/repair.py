from model.repair import OLDRepair
from crud.base import CrudBase
from sqlalchemy.orm import Session

class CrudRepair(CrudBase[OLDRepair]):
    def __init__(self, db: Session):
        super().__init__(model=OLDRepair, db=db)
        self.db
    
    def get_by_user_id_and_address_id(self, user_id: str, id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id, self.model.id == id).first()

    def get_by_user_id(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()
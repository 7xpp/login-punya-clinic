from crud.base import CrudBase
from model.address import OLDAddress
from sqlalchemy.orm import Session

class CrudAddress(CrudBase[OLDAddress]):
    def __init__(self, db: Session):
        super().__init__(model=OLDAddress, db=db)
        self.db

    def get_by_user_id(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()

    def get_by_count_user_id(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).count()

    def get_by_user_id_and_address_id(self, user_id, id):
        return self.db.query(self.model).filter(self.model.user_id == user_id, self.model.id == id).first()

    def get_by_address_id(self, address_id: str):
        return self.db.query(self.model).filter(self.model.id == address_id).first()

    def get_by_other_address(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id).order_by(self.model.created_at.desc()).first()

    def get_by_user_default_address(self, user_id: str):
        return self.db.query(self.model).filter(self.model.user_id == user_id, self.model.is_default == True).first()
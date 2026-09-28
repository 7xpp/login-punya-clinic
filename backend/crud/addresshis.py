from sqlalchemy.orm import Session
from model.addresshis import OLDAddressHistory
from crud.base import CrudBase

class CrudAddressHistory(CrudBase[OLDAddressHistory]):
    def __init__(self, db: Session):
        super().__init__(model=OLDAddressHistory, db=db)
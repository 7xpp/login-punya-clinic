from crud.repair import CrudRepair
from crud.resettel import CrudResetTel
from crud.current_user_id import CrudCurrentID
from crud.userdetail import CrudUserDetail
from sqlalchemy.orm import Session
from crud.auth import CrudAuth
from crud.forgotpassword import CrudFCC
from crud.reset_email import CrudResetEmail
from crud.changepassword import CrudChangePassword
from crud.address import CrudAddress
from crud.addresshis import CrudAddressHistory

class UnitOfWork:
    def __init__(self, db: Session):
        self.db = db

    def __enter__(self):
        self.current_user = CrudCurrentID(self.db)
        self.auth = CrudAuth(self.db)
        self.userdetail = CrudUserDetail(self.db)
        self.reset_email = CrudResetEmail(self.db)
        self.forgotpassword = CrudFCC(self.db)
        self.changepassword = CrudChangePassword(self.db)
        self.reset_tel = CrudResetTel(self.db)
        self.address = CrudAddress(self.db)
        self.addresshis = CrudAddressHistory(self.db)
        self.repair = CrudRepair(self.db)
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.rollback()
        
    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

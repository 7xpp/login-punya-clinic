from database.database import SessionLocal
from crud.unitofwork import UnitOfWork

def get_uow():
    db = SessionLocal()
    try:
        yield UnitOfWork(db)
    finally:
        db.close()
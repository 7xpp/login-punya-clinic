from fastapi.middleware.cors import CORSMiddleware
from database.database import engine, Base
from fastapi import FastAPI

import model.user
import model.address
import model.addresshis
import model.forgot_password
import model.reset_email
import model.repair

from api.address import router as address_router
from api.auth import router as auth_router
from api.changepassword import router as changepassword_router
from api.forgotpassword import router as forgotpassword_router
from api.repair import router as repair_router
from api.reset_email import router as reset_email_router
from api.resettel import router as reset_tel_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://127.0.0.1:8005"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(address_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(changepassword_router, prefix="/api/v1")
app.include_router(forgotpassword_router, prefix="/api/v1")
app.include_router(repair_router, prefix="/api/v1")
app.include_router(reset_email_router, prefix="/api/v1")
app.include_router(reset_tel_router, prefix="/api/v1")
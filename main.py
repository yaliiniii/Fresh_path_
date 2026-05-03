from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
import database
from routers import users, contact, appointments, habits, doctors, admin

app = FastAPI(title="FreshPath API")


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=database.engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI, APIRouter

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router)
api_router.include_router(doctors.router)
api_router.include_router(admin.router)
api_router.include_router(habits.router)
api_router.include_router(appointments.router)
api_router.include_router(contact.router)

@api_router.get("/")
def api_root():
    return {"message": "Welcome to FreshPath API"}

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
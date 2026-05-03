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

app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(admin.router)
app.include_router(habits.router)
app.include_router(appointments.router)
app.include_router(contact.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
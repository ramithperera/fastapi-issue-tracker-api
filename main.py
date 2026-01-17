from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.routes.auth import router as auth_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(timer_middleware) #

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router) #
app.include_router(issues_router) #
from app.routers.user import router as user_router
from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine

# Import all models
from app.models import User

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Cyber Threat Intelligence Platform"
)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine

# Import models
from app.models import User, IOC

# Import routers
from app.routers.user import router as user_router
from app.routers.ioc import router as ioc_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Cyber Threat Intelligence Platform"
)

# Register routers
app.include_router(user_router)
app.include_router(ioc_router)


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

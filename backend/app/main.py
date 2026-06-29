from fastapi import FastAPI 
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

@app.get("/")
async def root():
    return{
        "message":"GameDev AI Assistant API",
        "status": "running"
    }

@app.get("/health")
async def health():
    return{
        "status": "healthy"
    }
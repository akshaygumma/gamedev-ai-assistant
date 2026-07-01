from fastapi import FastAPI 
from app.core.config import settings
from app.api.projects import router as project_router
from app.api.llm import router as llm_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(project_router)
app.include_router(llm_router)

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


from fastapi import APIRouter

from app.schemas.project import Project
from app.workflows.project_creation_workflow import ProjectCreationWorkflow
from app.schemas.requests import CreateProjectRequest
from app.schemas.workflow_context import WorkflowContext
from app.core.workflow_registry import workflow_registry

from app.services.project_service import ProjectService

project_service = ProjectService()
router = APIRouter()

@router.post("/projects")
async def create_project(request: CreateProjectRequest):
    return project_service.create_project(name=request.name)

@router.get("/projects")
async def list_projects():
    return project_service.list_projects()

@router.get("/projects/{project_id}")
async def get_project_by_id(project_id: str):
    return project_service.get_project_by_id(project_id)
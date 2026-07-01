from fastapi import APIRouter

from app.schemas.project import Project
from app.workflows.project_creation_workflow import ProjectCreationWorkflow
from app.schemas.requests import CreateProjectRequest
from app.schemas.workflow_context import WorkflowContext
from app.core.workflow_registry import workflow_registry

router = APIRouter()

@router.post("/projects")
async def create_project(request: CreateProjectRequest):

    project = Project(
        name = request.name
    )

    context = WorkflowContext(project=project)

    workflow = workflow_registry.get("project_creation")

    context = workflow.run(context)

    return context.project
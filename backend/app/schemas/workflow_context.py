from pydantic import BaseModel

from app.schemas.project import Project

class WorkflowContext(BaseModel):
    project: Project
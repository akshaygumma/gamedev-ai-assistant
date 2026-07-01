from pydantic import BaseModel, Field
from app.schemas.project import Project

class WorkflowContext(BaseModel):

    project: Project

    request: dict = Field(default_factory=dict)

    response: dict = Field(default_factory=dict)
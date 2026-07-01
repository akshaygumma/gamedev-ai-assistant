from pydantic import BaseModel

class CreateProjectRequest(BaseModel):
    name: str

class WorkflowRequest(BaseModel):
    project_id: str
    user_id: str
    action: str
    data: dict
    payload: dict = {}

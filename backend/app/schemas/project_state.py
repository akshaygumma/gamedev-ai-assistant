from pydantic import BaseModel, Field
from app.schemas.requirements.requirement_state import RequirementState

class ProjectState(BaseModel):

    requirements: RequirementState = Field(default_factory=RequirementState)

    planning: dict = Field(default_factory=dict)

    implementation: dict = Field(default_factory=dict)

    builds: list = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)
from pydantic import BaseModel, Field


class ProjectState(BaseModel):

    requirements: dict = Field(default_factory=dict)

    planning: dict = Field(default_factory=dict)

    implementation: dict = Field(default_factory=dict)

    builds: list = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)
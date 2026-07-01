from typing import Any

from pydantic import BaseModel, Field

class RequirementState(BaseModel):

    extracted: dict[str, Any] = Field(default_factory=dict)
    missing: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    questions: list[str] = Field(default_factory=list)
    completed: bool = False
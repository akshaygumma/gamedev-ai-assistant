from datetime import datetime
from uuid import uuid4
from typing import Any
from app.schemas.project_state import ProjectState
from app.schemas.history import HistoryEntry

from pydantic import BaseModel, Field

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str

    current_stage: str = "created"

    state: ProjectState = Field(default_factory=ProjectState)

    history: list[HistoryEntry] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=datetime.utcnow)
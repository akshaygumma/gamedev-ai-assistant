from datetime import datetime

from pydantic import BaseModel, Field


class HistoryEntry(BaseModel):

    worker: str

    message: str

    timestamp: datetime = Field(default_factory=datetime.utcnow)
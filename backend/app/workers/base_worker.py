from abc import ABC, abstractmethod

from app.schemas.workflow_context import WorkflowContext

class BaseWorker(ABC):
    @abstractmethod
    def execute(self,context:WorkflowContext) -> WorkflowContext:
        pass
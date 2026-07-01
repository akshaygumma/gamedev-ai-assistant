from app.schemas.project import Project
from app.workers.base_worker import BaseWorker
from app.schemas.history import HistoryEntry
from app.schemas.workflow_context import WorkflowContext

class ProjectCreationWorker(BaseWorker):
    def execute(self,context: WorkflowContext) -> WorkflowContext:

        project = context.project   
        project.current_stage = "initialized"
        project.history.append(
            HistoryEntry(
                worker="ProjectCreationWorker",
                message="Project initialized."
            )
        )       

        context.project = project
        return context
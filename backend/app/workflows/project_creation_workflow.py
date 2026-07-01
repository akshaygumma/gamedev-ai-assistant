from app.workflows.base_workflow import BaseWorkflow
from app.workers.project_creation_worker import ProjectCreationWorker

class ProjectCreationWorkflow(BaseWorkflow):

    def __init__(self):
        super().__init__()

        self.workers = [
            ProjectCreationWorker()
        ]
from app.schemas.project import Project
from app.workers.base_worker import BaseWorker
from app.schemas.workflow_context import WorkflowContext

class BaseWorkflow:

    def __init__(self):

        self.workers: list[BaseWorker] = []

    def run(self, context: WorkflowContext):

        for worker in self.workers:

            context = worker.execute(context)

        return context
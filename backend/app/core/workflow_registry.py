from app.workflows.project_creation_workflow import ProjectCreationWorkflow

class WorkflowManager:

    def __init__(self):

        self.workflows = {
            "project_creation": ProjectCreationWorkflow
        }

    def get(self, workflow_name: str):

        workflow = self.workflows.get(workflow_name)

        if workflow is None:
            raise ValueError(f"Workflow '{workflow_name}' not found.")

        return workflow()

workflow_registry = WorkflowManager()
from app.database.repositories.project_repository import ProjectRepository
from app.schemas.project import Project

class ProjectService:
    def __init__(self):
        self.project_repository = ProjectRepository()

    def create_project(self, name: str):
        project = Project(name=name)
        return self.project_repository.create_project(project)

    def get_project_by_id(self, project_id: str):
        return self.project_repository.get_project_by_id(project_id)

    def list_projects(self):
        return self.project_repository.list()
from app.database.client import database_client
from app.schemas.project import Project

class ProjectRepository:
    TABLE_NAME = "projects"

    def create_project(self, project: Project):
        response = (database_client.client.table(self.TABLE_NAME).insert(project.model_dump(mode="json")).execute())

        return response.data[0] if response.data else None

    def get_project_by_id(self, project_id: str):
        response = (database_client.client.table(self.TABLE_NAME).select("*").eq("id", project_id).single().execute())
        
        return response.data if response.data else None

    def list(self):
        response = (database_client.client.table(self.TABLE_NAME).select("*").execute())
        
        return response.data if response.data else []
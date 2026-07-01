from supabase import Client, create_client

from app.core.config import settings

class DatabaseClient:
    def __init__(self):
        self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

database_client = DatabaseClient()
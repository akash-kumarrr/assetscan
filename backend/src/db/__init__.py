import os
from google.cloud import firestore
from google.oauth2 import service_account

class FirestoreClient:
    def __init__(self):
        self.key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "secrets/serviceAccountKey.json")

        self.creds = service_account.Credentials.from_service_account_file(self.key_path)

        self.client = firestore.AsyncClient(
            credentials=self.creds,
            project=self.creds.project_id
        )

    async def close(self):
        await self.client.close()

db_manager : FirestoreClient = None
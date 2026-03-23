from pydantic_settings import BaseSettings
import os
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Setting(BaseSettings):
    PROJECT_NAME : str = os.getenv("PROJECT_NAME")
    VERSION : str = "1.0.0"
    DEBUG : bool  = False
    SECRET_KEY : str = os.getenv("APP_SECRET_KEY")
    PROJECT_DESCRIPTION : str = "AssetScan is a professional utility designed to bridge the gap between physical hardware and digital records using high-speed QR technology."

    host: str = Field(default="0.0.0.0", alias="SERVER_HOST")
    port: int = Field(default=8000, alias="SERVER_PORT")

    firebase_db_url : str = "secrets/serviceAccountKey.json"


    class Config:
        env_file=".env"

setting = Setting()
    
import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_url: str = os.getenv("DB_URL")
    db_echo: bool = os.getenv("DB_ECHO")
    project_name: str = os.getenv("PROJECT_NAME")
    version: str = os.getenv("VERSION")


settings = Settings()

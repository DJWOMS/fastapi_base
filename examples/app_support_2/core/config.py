import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_echo: bool = os.getenv("DB_ECHO")
    project_name: str = os.getenv("PROJECT_NAME")
    version: str = os.getenv("VERSION")
    debug: bool = os.getenv("DEBUG")
    secret_key: str = os.environ.get("SECRET_KEY")
    cors_allowed_origins: str = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")


settings = Settings()

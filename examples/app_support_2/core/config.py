import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_ECHO: bool = os.getenv("DB_ECHO")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")
    DEBUG: bool = os.getenv("DEBUG")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    CORS_ALLOWED_ORIGINS: str


settings = Settings()

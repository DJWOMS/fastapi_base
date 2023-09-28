from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    SECRET_KEY: str
    CORS_ALLOWED_ORIGINS: str


settings = Settings()

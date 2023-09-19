from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = True
    project_name: str = "Support"
    version: str = "0.0.1"


settings = Settings()

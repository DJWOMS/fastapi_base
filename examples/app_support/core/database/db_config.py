from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv()


class ConfigDataBase(BaseSettings):
    db_url: str
    db_echo: bool


settings_db = ConfigDataBase()

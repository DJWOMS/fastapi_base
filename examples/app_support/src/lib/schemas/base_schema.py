from pydantic import BaseModel


class Base(BaseModel):
    """Базовая схема Pydantic.
    С поддержкой ORM
    """
    class Config:
        from_attributes = True


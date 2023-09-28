from typing import NewType

from pydantic import BaseModel


class Base(BaseModel):
    """Базовая схема Pydantic

    """
    class Config:
        from_attributes = True


PyModel = NewType("PyModel", Base)

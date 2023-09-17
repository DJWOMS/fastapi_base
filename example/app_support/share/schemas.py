from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        from_attributes = True

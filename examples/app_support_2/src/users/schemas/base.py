from pydantic import BaseModel

from core.share.schemas import Base


class PermissionBase(BaseModel):
    name: str
    code: int


class UserBase(Base):
    username: str

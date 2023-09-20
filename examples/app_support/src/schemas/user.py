from pydantic import BaseModel, EmailStr

from ..share.schemas import Base


class PermissionBase(BaseModel):
    name: str
    code: int


class PermissionCreate(PermissionBase):
    pass


class PermissionResponse(PermissionBase):
    id: int


class UserBase(Base):
    username: str


class UserCreate(UserBase):
    permission_id: int
    email: EmailStr
    password: str


class CreateSuperUser(UserBase):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    permission: PermissionBase

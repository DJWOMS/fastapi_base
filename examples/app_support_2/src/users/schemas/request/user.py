from pydantic import EmailStr

from ..base import UserBase


class UserCreate(UserBase):
    permission_id: int
    email: EmailStr
    password: str


class CreateSuperUser(UserBase):
    email: EmailStr
    password: str

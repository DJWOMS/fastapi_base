from pydantic import BaseModel, EmailStr

from ..base import PermissionBase


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    permission: PermissionBase

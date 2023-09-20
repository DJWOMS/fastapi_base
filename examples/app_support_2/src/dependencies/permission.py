from fastapi import Depends, HTTPException

from ..share.permissions import AbstractPermission

from ..services.auth import AuthService
from ..models.user import User


class Permission(AbstractPermission):
    def __init__(self, permission: str) -> None:
        self.permission = permission

    def __call__(self, user: User = Depends(AuthService())) -> User | HTTPException:
        return self.check_permissions(user)

    def check_permissions(self, user: User) -> User | HTTPException:
        print(self.permission, user.permission.name)
        if self.permission == user.permission.name:
            return user

        raise HTTPException(status_code=403, detail="User doesn't have enough rights")


is_manager = Permission("manager")
is_admin = Permission("admin")

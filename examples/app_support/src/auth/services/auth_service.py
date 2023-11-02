from abc import ABC

from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from ...config.database.db_helper import db_helper

from ...dtos.user_dto import UserSchema



oauth2_scheme = APIKeyHeader(name="role")


class AbstractAuthService(ABC):
    def __call__(self):
        raise NotImplementedError


class AuthService:
    def __init__(self, role: str):
        self.role = role

    def __call__(
            self,
            role: str = Depends(oauth2_scheme),
            db_session: Session = Depends(db_helper.get_session)
    ):
        if self.role == role:
            # user = user_repository(db_session, role=role)
            # return UserSchema.model_validate(user, from_attributes=True)
            return UserSchema(id=1, username="John", role=role)
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


is_admin = AuthService("admin")
is_client = AuthService("client")
is_manager = AuthService("manager")

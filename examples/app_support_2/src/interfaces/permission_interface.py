from abc import ABC
from typing import NewType

from ..models.base_model import Base


UserModel = NewType("UserModel", Base)


class AbstractPermission(ABC):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def check_permissions(self, user: UserModel) -> UserModel:
        raise NotImplementedError

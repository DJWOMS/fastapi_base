from abc import ABC

from core.share.controller_base.base import UserModel


class AbstractPermission(ABC):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def check_permissions(self, user: UserModel) -> UserModel:
        raise NotImplementedError

from src.services.base_service import BaseService
from ..repositories.support_repository import support_repository


class SupportService(BaseService):
    pass


support_service = SupportService(repository=support_repository)

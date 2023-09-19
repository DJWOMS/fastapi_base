from ..share.service import BaseService
from ..repositories.support import support_repository, category_repository


class CategoryService(BaseService):

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


class SupportService(BaseService):
    pass


category_service = CategoryService(repository=category_repository)
support_service = SupportService(repository=support_repository)

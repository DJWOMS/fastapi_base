from core.share.repository import SqlModel
from core.share.service import BaseService
from .repositories import support_repository, category_repository


class CategoryService(BaseService):

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[SqlModel] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


class SupportService(BaseService):
    pass


category_service = CategoryService(repository=category_repository)
support_service = SupportService(repository=support_repository)

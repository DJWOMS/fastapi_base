from .schemas import PyModel
from .repository import AbstractRepository, SqlModel


class BaseService:

    def __init__(self, repository: AbstractRepository) -> None:
        self.repository: AbstractRepository = repository

    async def create(self, model: PyModel) -> SqlModel:
        return await self.repository.create(data=model.model_dump())

    async def update(self, pk: int, model: PyModel) -> SqlModel:
        return await self.repository.update(data=model.model_dump(), id=pk)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(id=pk)

    async def get(self, pk: int) -> SqlModel:
        return await self.repository.get(id=pk)

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

    # async def bulk_add(self, model: List[PyModel]):
    #     data = [model_data.model_dump() for model_data in model]
    #     try:
    #         return await self.repository.bulk_create(data)
    #     except AlreadyExistError as e:
    #         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    #
    # async def get_or_add(self, pk, data: dict):
    #     try:
    #         return await self.repository.get_single(id=pk)
    #     except NoRowsFoundError:
    #         await self.repository.create(data)
    #     return await self.repository.get_single(id=pk)
    #
    # async def all(self):
    #     return await self.repository.all()
    #

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from core.database.db_helper import AsyncDatabaseSession

from share.schemas import PyModel
from share.errors import (
    AlreadyExistError,
    DBError,
    MultipleRowsFoundError,
    NoRowsFoundError,
)
from share.repository import SqlAlchemyRepository


class BaseService:
    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository = repository

    async def create(self, model: PyModel = None) -> object:
        return await self.repository.create(model.model_dump())

    # async def bulk_add(self, model: list[PyModel], user: UserModel = None):
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
    # async def all(self, user: UserModel = None):
    #     return await self.repository.all()
    #
    # async def filter(self, user: UserModel = None, filters: dict = None):
    #     return await self.repository.filter(filters=filters)
    #
    # async def retrieve(self, pk, model: PyModel = None, user: UserModel = None):
    #     try:
    #         return await self.repository.get_single(id=pk)
    #     except (NoRowsFoundError, MultipleRowsFoundError):
    #         raise HTTPException(HTTP_404_NOT_FOUND)
    #
    # async def update(self, pk, model: PyModel = None, user: UserModel = None):
    #     try:
    #         return await self.repository.update(model.model_dump(), {"id": pk})
    #     except NoRowsFoundError as e:
    #         raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")
    #     except (DBError, AlreadyExistError) as e:
    #         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    #
    # async def partial_update(self, pk, model: PyModel = None, user: UserModel = None):
    #     data = model.model_dump(exclude_unset=True)
    #     try:
    #         return await self.repository.update(data, {"id": pk})
    #     except NoRowsFoundError as e:
    #         raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")
    #     except (DBError, AlreadyExistError) as e:
    #         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    #
    # async def delete(self, pk, model: PyModel = None, user: UserModel = None):
    #     try:
    #         return await self.repository.delete(id=pk)
    #     except NoRowsFoundError as e:
    #         raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")



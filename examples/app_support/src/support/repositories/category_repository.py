from sqlalchemy import select, ScalarResult, exc, desc, Select, update, delete

from ..dependencies.repository_depends import IAsyncSession
from ..models.category_model import CategoryModel
from ..dtos.category_dto import CategoryListDto, CategoryDto, CategoryCreateDto, CategoryUpdateDto
from ...exceptions import AlreadyExistError


class CategoryRepository:
    """Репозиторий категорий"""
    model = CategoryModel

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create(self, dto: CategoryCreateDto) -> CategoryDto:
        instance = self.model(**dto.model_dump())
        self._session.add(instance)
        try:
            await self._session.commit()
        except exc.IntegrityError as e:
            raise AlreadyExistError("Запись уже существует")
        await self._session.refresh(instance)
        return self._get_dto(instance)

    async def update(self, pk: int, dto: CategoryUpdateDto) -> CategoryDto:
        stmt = (
            update(self.model)
            .where(self.model.id == pk)
            .values(**dto.model_dump())
            .returning(self.model)
        )
        res = await self._session.execute(stmt)
        await self._session.commit()
        return self._get_dto(res.scalar_one())

    async def delete(self, pk: int) -> None:
        stmt = delete(self.model).where(self.model.id == pk)
        res = await self._session.execute(stmt)
        if res.rowcount == 0:
            raise exc.NoResultFound(f'Запись в таблице {self.model.__tablename__} не найдена')
        await self._session.commit()

    def _order(self, stmt: Select, order: str = 'id') -> Select:
        match order:
            case s if s.startswith('-'):
                stmt = stmt.order_by(order[1:])
            case _:
                stmt = stmt.order_by(desc(order))
        return stmt

    async def get_multi(
            self,
            order: str = 'id',
            limit: int = 100,
            offset: int = 0,
    ) -> list[CategoryListDto] | None:
        stmt = select(self.model).limit(limit).offset(offset)
        stmt = self._order(stmt, order)
        res = await self._session.execute(stmt)
        return self._get_list_dto(res.scalars())

    def _get_list_dto(self, row: ScalarResult) -> list[CategoryListDto]:
        return [CategoryListDto(**model.__dict__) for model in row]

    def _get_dto(self, row: CategoryModel) -> CategoryDto:
        return CategoryDto(**row.__dict__)

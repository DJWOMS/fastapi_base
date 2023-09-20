from sqlalchemy import select
from sqlalchemy.orm import load_only

from core.share.repository import SqlAlchemyRepository, SqlModel
from .models import Support, Category
from core.database.db_helper import db_helper




class CategoryRepository(SqlAlchemyRepository):
    model = Category

    async def filter(
        self,
        fields: list[str] | None = None,
        order: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[SqlModel] | None:
        async with self._session_factory() as session:
            stmt = select(self.model)
            if fields:
                model_fields = [getattr(self.model, field) for field in fields]
                stmt = stmt.options(load_only(*model_fields))
            if order:
                stmt = stmt.order_by(*order)
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            row = await session.execute(stmt)
            return row.scalars().all()

    async def all(self) -> list[SqlModel] | None:
        return await self.filter()

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        async with self._session_factory() as session:
            result = await session.execute(stmt)
            return result.scalar() is not None


class SupportRepository(SqlAlchemyRepository):
    model = Support


category_repository = CategoryRepository(db_session=db_helper.get_db_session)
support_repository = SupportRepository(db_session=db_helper.get_db_session)

from ..share.repository import SqlAlchemyRepository
from ..models.support import Support, Category
from core.database.db_helper import db_helper


class CategoryRepository(SqlAlchemyRepository):
    model = Category


class SupportRepository(SqlAlchemyRepository):
    model = Support


category_repository = CategoryRepository(db_session=db_helper.get_db_session)
support_repository = SupportRepository(db_session=db_helper.get_db_session)

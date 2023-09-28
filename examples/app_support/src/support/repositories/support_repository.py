from src.lib.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.config.database.db_helper import db_helper

from ..models.support_model import SupportModel


class SupportRepository(SqlAlchemyRepository):
    model = SupportModel


support_repository = SupportRepository(db_session=db_helper.get_db_session)

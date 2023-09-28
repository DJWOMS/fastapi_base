from src.lib.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.config.database.db_helper import db_helper

from ..models.support_model import SupportModel
from ..schemas.support_schema import SupportCreate, SupportUpdate


class SupportRepository(SqlAlchemyRepository[SupportModel, SupportCreate, SupportUpdate]):
    pass


support_repository = SupportRepository(model=SupportModel, db_session=db_helper.get_db_session)

from core.database import db_helper
from share.repository import AbstractRepository
from share.service import BaseService


class GenericService:
    def __init__(self, model, service=BaseService, repository=AbstractRepository):
        self._model = model

        class Repository(repository):
            model = self._model

        self._repository = Repository(db_session=db_helper.get_db_session)
        self._service = service(repository=self._repository)

    @property
    def get_service(self):
        return self._service

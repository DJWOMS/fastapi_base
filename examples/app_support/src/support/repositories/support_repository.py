from ..dependencies.repository_depends import IAsyncSession
from ..models.support_model import RequestSupportModel
from ..dtos.support_dto import CreateClientSupportDto, ClientSupportDto


class SupportRepository:
    """Репозиторий поддержки"""
    model = RequestSupportModel

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create(self, dto: CreateClientSupportDto) -> ClientSupportDto:
        instance = self.model(**dto.model_dump())
        self._session.add(instance)
        await self._session.flush()
        await self._session.commit()
        await self._session.refresh(instance)
        return self._get_dto(instance)

    def _get_dto(self, row: RequestSupportModel) -> ClientSupportDto:
        return ClientSupportDto(**row.__dict__)

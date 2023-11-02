from ..dependencies.services_depends import ISupportRepository
from ..dtos.support_dto import ClientSupportDto, CreateClientSupportDto


class SupportService:
    """Сервис для работы с поддержкой"""

    def __init__(self, repository: ISupportRepository) -> None:
        self.repository = repository

    async def create(self, dto: CreateClientSupportDto) -> ClientSupportDto:
        return await self.repository.create(dto=dto)

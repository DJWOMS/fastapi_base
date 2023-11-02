from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_400_BAD_REQUEST

from ..dtos.support_dto import CreateClientSupportDto, ClientSupportDto
from ..services.support_services import SupportService

router = APIRouter(prefix='/support', tags=["client"])


@router.post("/")
async def create_support(
        dto: CreateClientSupportDto,
        service: SupportService = Depends()
) -> ClientSupportDto:
    """Создание заявки не авторизованным пользователем"""
    return await service.create(dto=dto)

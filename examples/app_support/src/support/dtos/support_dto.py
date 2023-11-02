from pydantic import BaseModel, EmailStr


class SupportBase(BaseModel):
    category_id: int
    text: str


class CreateClientSupportDto(SupportBase):
    username: str
    email: EmailStr


class UpdateSupportDto(SupportBase):
    pass


class ClientSupportDto(SupportBase):
    id: int
    username: str
    email: EmailStr

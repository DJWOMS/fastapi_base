from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """Абстрактный репозиторий для работы с базой данных

    """
    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_single(self, **kwargs):
        raise NotImplementedError

    async def get_multi(self, **kwargs):
        raise NotImplementedError

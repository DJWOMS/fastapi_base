from abc import ABC, abstractmethod


class AbstractQueryRepository(ABC):
    """Абстрактный Query репозиторий для работы с базой данных

    """

    @abstractmethod
    async def get_single(self, **kwargs):
        raise NotImplementedError

    async def get_multi(self, **kwargs):
        raise NotImplementedError

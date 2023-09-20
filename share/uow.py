from abc import abstractmethod, ABC


class UnitOfWork(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        async with self.session_factory() as session:
            self.session = session
            return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

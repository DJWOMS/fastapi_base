from .base_uow import UnitOfWork


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

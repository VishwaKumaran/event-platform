from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from sqlmodel import SQLModel


def create_db_engine(postgresql_uri: str, debug: bool = False):
    return create_async_engine(postgresql_uri, echo=debug, future=True)


def create_session_factory(engine):
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def init_db(engine):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


class Database:
    def __init__(self, postgresql_uri: str, debug: bool = False):
        self.engine = create_db_engine(postgresql_uri, debug=debug)
        self.session_factory = create_session_factory(self.engine)

    async def init_db(self):
        await init_db(self.engine)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    @asynccontextmanager
    async def get_session_context(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

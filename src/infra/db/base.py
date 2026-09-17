import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


from src.config import PGSettings

logger = logging.getLogger(__name__)

engine = create_async_engine(
    PGSettings.build_dsn(),
    poolclass=NullPool,
    connect_args={"server_settings": {"jit": "off"}},
)


@asynccontextmanager
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session

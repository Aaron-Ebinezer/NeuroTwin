from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()
DB_URL = os.getenv("DATABASE_URL","sqlite+aiosqlite:///./data/tutor.db")
engine = create_async_engine(
    DB_URL,
    echo = False,
    pool_size = 10,
    max_overflow = 20,
    connect_args = {"check same thread": False}
)

AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit = False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
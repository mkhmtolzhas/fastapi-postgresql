from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .config import settings, Settings


class Database:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.engine = create_async_engine(settings.database_url)
        self.session = async_sessionmaker(self.engine, class_=AsyncSession)


    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(DeclarativeBase.metadata.create_all)

    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(DeclarativeBase.metadata.drop_all)
    
    async def get_session(self):
        async with self.session() as session:
            yield session


database = Database(settings)

class Base(DeclarativeBase):
    pass

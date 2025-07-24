from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/budget_horizon")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Dependency для FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session 
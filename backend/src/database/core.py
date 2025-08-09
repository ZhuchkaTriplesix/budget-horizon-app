from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from fastapi import Request
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/budget_horizon")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Dependency для FastAPI, использует сессию из middleware если есть
async def get_db(request: Request):
    session = getattr(request.state, "db", None)
    if session is not None:
        yield session
        return
    async with AsyncSessionLocal() as new_session:
        yield new_session
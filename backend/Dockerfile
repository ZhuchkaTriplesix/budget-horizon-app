FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./alembic.ini ./alembic.ini
RUN mkdir -p alembic && touch alembic/README
COPY ./alembic ./alembic

ENV DATABASE_URL=postgresql+asyncpg://user:password@db:5432/budget_horizon \
    REDIS_URL=redis://redis:6379 \
    UVICORN_HOST=0.0.0.0 \
    UVICORN_PORT=8000

CMD alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000



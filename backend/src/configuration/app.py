from fastapi import FastAPI

from src.routers import Router
from src.database.core import engine, Base


class App:
    def __init__(self) -> None:
        self.app = FastAPI(title="Budget Horizon API")
        self._include_routers()
        self._register_events()

    def _include_routers(self) -> None:
        for router, prefix, tags in Router.routers:
            self.app.include_router(router, prefix=prefix, tags=tags)

    def _register_events(self) -> None:
        @self.app.on_event("startup")
        async def on_startup() -> None:
            # Создаём таблицы, если их ещё нет (на случай, если миграций нет).
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)



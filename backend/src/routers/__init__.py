from dataclasses import dataclass

from src.routers.cart.router import router as cart_router
from src.routers.domain.router import router as domain_router
from src.routers.user.router import router as user_router


@dataclass(frozen=True)
class Router:
    routers = [
        (user_router, "/api/user", ["user"])
    ]
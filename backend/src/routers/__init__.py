from dataclasses import dataclass

from src.routers.user.routes import router as user_router
from src.routers.category.routes import router as category_router
from src.routers.transaction.routes import router as transaction_router
from src.routers.budget.routes import router as budget_router
from src.routers.tag.routes import router as tag_router

@dataclass(frozen=True)
class Router:
    routers = [
        (user_router, "/api/user", ["user"]),
        (category_router, "/api/category", ["category"]),
        (transaction_router, "/api/transaction", ["transaction"]),
        (budget_router, "/api/budget", ["budget"]),
        (tag_router, "/api/tag", ["tag"]),
    ]
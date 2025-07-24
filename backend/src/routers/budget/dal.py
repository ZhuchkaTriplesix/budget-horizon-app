from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Budget

class BudgetDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_budget(self, user_id: int, category_id: int, amount_limit: float, period_start, period_end) -> Budget:
        budget = Budget(user_id=user_id, category_id=category_id, amount_limit=amount_limit, period_start=period_start, period_end=period_end)
        self.session.add(budget)
        await self.session.flush()
        return budget

    async def get_budget_by_id(self, budget_id: int) -> Optional[Budget]:
        res = await self.session.execute(select(Budget).where(Budget.id == budget_id))
        row = res.fetchone()
        return row[0] if row else None

    async def get_budgets_by_user(self, user_id: int) -> List[Budget]:
        res = await self.session.execute(select(Budget).where(Budget.user_id == user_id))
        return [row[0] for row in res.fetchall()]

    async def update_budget(self, budget_id: int, **kwargs) -> Optional[Budget]:
        query = update(Budget).where(Budget.id == budget_id).values(**kwargs).returning(Budget)
        res = await self.session.execute(query)
        row = res.fetchone()
        return row[0] if row else None

    async def delete_budget(self, budget_id: int) -> None:
        await self.session.execute(delete(Budget).where(Budget.id == budget_id)) 
from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Category

class CategoryDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_category(self, user_id: int, name: str, type: str) -> Category:
        category = Category(user_id=user_id, name=name, type=type)
        self.session.add(category)
        await self.session.flush()
        return category

    async def get_category_by_id(self, category_id: int) -> Optional[Category]:
        res = await self.session.execute(select(Category).where(Category.id == category_id))
        row = res.fetchone()
        return row[0] if row else None

    async def get_categories_by_user(self, user_id: int) -> List[Category]:
        res = await self.session.execute(select(Category).where(Category.user_id == user_id))
        return [row[0] for row in res.fetchall()]

    async def update_category(self, category_id: int, name: Optional[str] = None, type: Optional[str] = None) -> Optional[Category]:
        values = {}
        if name is not None:
            values['name'] = name
        if type is not None:
            values['type'] = type
        query = update(Category).where(Category.id == category_id).values(**values).returning(Category)
        res = await self.session.execute(query)
        row = res.fetchone()
        return row[0] if row else None

    async def delete_category(self, category_id: int) -> None:
        await self.session.execute(delete(Category).where(Category.id == category_id)) 
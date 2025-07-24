from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Category
from .schemas import CategoryCreate

async def get_categories(db: AsyncSession, user_id: int):
    result = await db.execute(select(Category).where(Category.user_id == user_id))
    return result.scalars().all()

async def create_category(db: AsyncSession, user_id: int, category: CategoryCreate):
    db_category = Category(user_id=user_id, **category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category 
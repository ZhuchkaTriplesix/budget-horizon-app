from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Tag

class TagDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_tag(self, user_id: int, name: str) -> Tag:
        tag = Tag(user_id=user_id, name=name)
        self.session.add(tag)
        await self.session.flush()
        return tag

    async def get_tag_by_id(self, tag_id: int) -> Optional[Tag]:
        res = await self.session.execute(select(Tag).where(Tag.id == tag_id))
        row = res.fetchone()
        return row[0] if row else None

    async def get_tags_by_user(self, user_id: int) -> List[Tag]:
        res = await self.session.execute(select(Tag).where(Tag.user_id == user_id))
        return [row[0] for row in res.fetchall()]

    async def update_tag(self, tag_id: int, name: str) -> Optional[Tag]:
        query = update(Tag).where(Tag.id == tag_id).values(name=name).returning(Tag)
        res = await self.session.execute(query)
        row = res.fetchone()
        return row[0] if row else None

    async def delete_tag(self, tag_id: int) -> None:
        await self.session.execute(delete(Tag).where(Tag.id == tag_id)) 
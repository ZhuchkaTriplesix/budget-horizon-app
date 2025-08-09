from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import TagDAL
from .schemas import Tag, TagCreate
from src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Tag)
async def create_tag(tag: TagCreate, db: AsyncSession = Depends(get_db)):
    dal = TagDAL(db)
    obj = await dal.create_tag(user_id=tag.user_id, name=tag.name)
    return obj

@router.get("/user/{user_id}", response_model=List[Tag])
async def get_tags_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    dal = TagDAL(db)
    return await dal.get_tags_by_user(user_id)

@router.get("/{tag_id}", response_model=Tag)
async def get_tag(tag_id: int, db: AsyncSession = Depends(get_db)):
    dal = TagDAL(db)
    obj = await dal.get_tag_by_id(tag_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    return obj

@router.put("/{tag_id}", response_model=Tag)
async def update_tag(tag_id: int, tag: TagCreate, db: AsyncSession = Depends(get_db)):
    dal = TagDAL(db)
    obj = await dal.update_tag(tag_id, name=tag.name)
    if not obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    return obj

@router.delete("/{tag_id}")
async def delete_tag(tag_id: int, db: AsyncSession = Depends(get_db)):
    dal = TagDAL(db)
    await dal.delete_tag(tag_id)
    return {"ok": True} 
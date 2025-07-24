from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import CategoryDAL
from .schemas import Category, CategoryCreate
from backend.src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Category)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    dal = CategoryDAL(db)
    obj = await dal.create_category(user_id=category.user_id, name=category.name, type=category.type)
    return obj

@router.get("/user/{user_id}", response_model=List[Category])
async def get_categories_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    dal = CategoryDAL(db)
    return await dal.get_categories_by_user(user_id)

@router.get("/{category_id}", response_model=Category)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    dal = CategoryDAL(db)
    obj = await dal.get_category_by_id(category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj

@router.put("/{category_id}", response_model=Category)
async def update_category(category_id: int, category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    dal = CategoryDAL(db)
    obj = await dal.update_category(category_id, name=category.name, type=category.type)
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj

@router.delete("/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    dal = CategoryDAL(db)
    await dal.delete_category(category_id)
    return {"ok": True} 
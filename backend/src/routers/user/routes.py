from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import UserDAL
from .schemas import User, UserCreate
from backend.src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    dal = UserDAL(db)
    obj = await dal.create_user(email=user.email, phone_number=user.phone_number, password=user.password)
    return obj

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    dal = UserDAL(db)
    # Здесь предполагается, что UserDAL реализует get_user_by_id
    obj = await dal.get_user_by_id(user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj 
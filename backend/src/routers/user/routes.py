from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import UserDAL
from .schemas import User, UserCreate
from src.security.security import Security
from fastapi import Response
from src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, response: Response, db: AsyncSession = Depends(get_db)):
    dal = UserDAL(db)
    obj = await dal.create_user(email=user.email, phone_number=user.phone_number, password=user.password)
    # Создаём сессию и кладём cookie (совместимо с вашей текущей Security)
    token = await Security.create_session(user_id=obj.id, email=obj.email, permission="user")
    response.set_cookie(key="session_id", value=token, httponly=True, samesite="lax")
    return obj

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    dal = UserDAL(db)
    # Здесь предполагается, что UserDAL реализует get_user_by_id
    obj = await dal.get_user_by_id(user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj 
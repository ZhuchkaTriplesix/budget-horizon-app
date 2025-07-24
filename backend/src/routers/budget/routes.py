from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import BudgetDAL
from .schemas import Budget, BudgetCreate
from backend.src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Budget)
async def create_budget(budget: BudgetCreate, db: AsyncSession = Depends(get_db)):
    dal = BudgetDAL(db)
    obj = await dal.create_budget(
        user_id=budget.user_id,
        category_id=budget.category_id,
        amount_limit=budget.amount_limit,
        period_start=budget.period_start,
        period_end=budget.period_end
    )
    return obj

@router.get("/user/{user_id}", response_model=List[Budget])
async def get_budgets_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    dal = BudgetDAL(db)
    return await dal.get_budgets_by_user(user_id)

@router.get("/{budget_id}", response_model=Budget)
async def get_budget(budget_id: int, db: AsyncSession = Depends(get_db)):
    dal = BudgetDAL(db)
    obj = await dal.get_budget_by_id(budget_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Budget not found")
    return obj

@router.put("/{budget_id}", response_model=Budget)
async def update_budget(budget_id: int, budget: BudgetCreate, db: AsyncSession = Depends(get_db)):
    dal = BudgetDAL(db)
    obj = await dal.update_budget(budget_id, **budget.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Budget not found")
    return obj

@router.delete("/{budget_id}")
async def delete_budget(budget_id: int, db: AsyncSession = Depends(get_db)):
    dal = BudgetDAL(db)
    await dal.delete_budget(budget_id)
    return {"ok": True} 
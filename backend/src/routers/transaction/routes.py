from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dal import TransactionDAL
from .schemas import Transaction, TransactionCreate
from src.database.core import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Transaction)
async def create_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    dal = TransactionDAL(db)
    obj = await dal.create_transaction(
        user_id=transaction.user_id,
        category_id=transaction.category_id,
        amount=transaction.amount,
        description=transaction.description,
        date=transaction.date
    )
    return obj

@router.get("/user/{user_id}", response_model=List[Transaction])
async def get_transactions_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    dal = TransactionDAL(db)
    return await dal.get_transactions_by_user(user_id)

@router.get("/{transaction_id}", response_model=Transaction)
async def get_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    dal = TransactionDAL(db)
    obj = await dal.get_transaction_by_id(transaction_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return obj

@router.put("/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: int, transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    dal = TransactionDAL(db)
    obj = await dal.update_transaction(transaction_id, **transaction.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return obj

@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: int, db: AsyncSession = Depends(get_db)):
    dal = TransactionDAL(db)
    await dal.delete_transaction(transaction_id)
    return {"ok": True} 
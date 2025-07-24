from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    date: Optional[datetime] = None
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True 
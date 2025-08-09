from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: int
    amount: float
    description: Optional[str] = None
    date: Optional[datetime] = None
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
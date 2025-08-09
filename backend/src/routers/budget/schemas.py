from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BudgetBase(BaseModel):
    amount_limit: float
    period_start: datetime
    period_end: datetime
    category_id: int

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    type: str
    user_id: int

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True 
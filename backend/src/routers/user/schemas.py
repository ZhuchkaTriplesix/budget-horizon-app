from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    phone_number: str
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    is_verify: bool
    class Config:
        orm_mode = True 
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID
    email: str
    permission: str
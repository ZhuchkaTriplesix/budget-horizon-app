from sqlalchemy import Integer, String, ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.core import Base
from uuid import UUID

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[UUID] = mapped_column(types.UUID, ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)  # 'income' or 'expense'
    user = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")
    budgets = relationship("Budget", back_populates="category") 
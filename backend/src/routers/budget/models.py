from sqlalchemy import Integer, ForeignKey, Numeric, DateTime, types
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.core import Base
from datetime import datetime
from uuid import UUID

class Budget(Base):
    __tablename__ = "budgets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[UUID] = mapped_column(types.UUID, ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    amount_limit: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets") 
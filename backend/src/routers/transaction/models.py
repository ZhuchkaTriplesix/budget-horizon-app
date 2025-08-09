from sqlalchemy import Integer, ForeignKey, Numeric, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.core import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions") 
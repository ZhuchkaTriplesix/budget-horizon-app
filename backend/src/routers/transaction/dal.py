from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Transaction

class TransactionDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_transaction(self, user_id: int, category_id: int, amount: float, description: str, date) -> Transaction:
        transaction = Transaction(user_id=user_id, category_id=category_id, amount=amount, description=description, date=date)
        self.session.add(transaction)
        await self.session.flush()
        return transaction

    async def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        res = await self.session.execute(select(Transaction).where(Transaction.id == transaction_id))
        row = res.fetchone()
        return row[0] if row else None

    async def get_transactions_by_user(self, user_id: int) -> List[Transaction]:
        res = await self.session.execute(select(Transaction).where(Transaction.user_id == user_id))
        return [row[0] for row in res.fetchall()]

    async def update_transaction(self, transaction_id: int, **kwargs) -> Optional[Transaction]:
        query = update(Transaction).where(Transaction.id == transaction_id).values(**kwargs).returning(Transaction)
        res = await self.session.execute(query)
        row = res.fetchone()
        return row[0] if row else None

    async def delete_transaction(self, transaction_id: int) -> None:
        await self.session.execute(delete(Transaction).where(Transaction.id == transaction_id)) 
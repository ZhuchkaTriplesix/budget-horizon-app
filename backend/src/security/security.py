import json
from uuid import UUID

from fastapi import HTTPException, Cookie
from starlette import status

from src.misc.misc import generate_token
from src.redis.redis import RedisController
from src.schemas import User


class Security:
    @staticmethod
    async def create_session(user_id: UUID, email: str, permission: str) -> str:
        data = {
            'user_id': str(user_id),
            "email": email,
            "permission": permission
        }
        token = await generate_token()
        await RedisController().set_record(tag="session", key=token, value=str(data).replace("'", '"'))
        return token

    @staticmethod
    async def session_user_verify(session_id: str = Cookie(None)) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
        record = await RedisController.get_record(tag="session", key=session_id)
        if record is None:
            raise credentials_exception
        try:
            record = json.loads(record)
            user_id: UUID = record['user_id']
            email: str = record.get("email")
            permission: str = record.get("permission")
        except Exception:
            raise credentials_exception
        if permission == "user":
            return User(
                user_id=user_id,
                email=email,
                permission=permission
            )
        raise credentials_exception
from typing import List, Dict, Optional, Union

from redis.asyncio import Redis

from src import config

r: Redis = Redis(decode_responses=True, **config.redis.dict())


class RedisController:

    @classmethod
    async def set_record(cls, tag: str, key: str, value: Union[Dict, str], ex: int = 5400) -> None:
        await r.set(name=f"{tag}:{key}", value=value, ex=ex)

    @classmethod
    async def get_record(cls, tag: str, key: str) -> Optional[str]:
        return await r.get(name=f"{tag}:{key}")

    @classmethod
    async def del_record(cls, tag: str, key: str) -> None:
        await r.delete(f"{tag}:{key}")

    @classmethod
    async def get_all_values(cls) -> Optional[Dict]:
        keys = await cls._get_all_keys()
        if len(keys) == 0:
            return
        values = await r.mget(*await cls._get_all_keys())
        return dict(zip(keys, values))

    @classmethod
    async def _get_all_keys(cls) -> List[str]:
        return await r.keys("*")

    @classmethod
    async def get_all_values_by_tag(cls, tag: str) -> Dict:
        all_keys = await cls._get_all_keys()
        keys = [key for key in all_keys if str(key).startswith(f"{tag}:")]

        if not keys:
            return {}

        values = await r.mget(*keys)
        return dict(zip(keys, values))
from abc import ABC
from dataclasses import asdict, dataclass
import configparser
import os

config = configparser.ConfigParser()
config.read("config.ini")


class CfgBase(ABC):
    dict: callable = asdict


class PostgresCfg(CfgBase):
    def __init__(self):
        self.database: str = os.getenv("DB_DIALECT", config["POSTGRES"]["DATABASE"]) if config.has_section("POSTGRES") else os.getenv("DB_DIALECT", "postgresql")
        self.driver: str = os.getenv("DB_DRIVER", config["POSTGRES"]["DRIVER"]) if config.has_section("POSTGRES") else os.getenv("DB_DRIVER", "asyncpg")
        self.database_name: str = os.getenv("POSTGRES_DB", config["POSTGRES"]["DATABASE_NAME"]) if config.has_section("POSTGRES") else os.getenv("POSTGRES_DB", "budget_horizon")
        self.username: str = os.getenv("POSTGRES_USER", config["POSTGRES"]["USERNAME"]) if config.has_section("POSTGRES") else os.getenv("POSTGRES_USER", "user")
        self.password: str = os.getenv("POSTGRES_PASSWORD", config["POSTGRES"]["PASSWORD"]) if config.has_section("POSTGRES") else os.getenv("POSTGRES_PASSWORD", "password")
        self.ip: str = os.getenv("POSTGRES_HOST", config["POSTGRES"]["IP"]) if config.has_section("POSTGRES") else os.getenv("POSTGRES_HOST", "db")
        self.port: int = int(os.getenv("POSTGRES_PORT", str(config.getint("POSTGRES", "PORT"))) if config.has_section("POSTGRES") else os.getenv("POSTGRES_PORT", "5432"))

        self.database_engine_pool_timeout: int = config.getint("POSTGRES", "DATABASE_ENGINE_POOL_TIMEOUT")
        self.database_engine_pool_recycle: int = config.getint("POSTGRES", "DATABASE_ENGINE_POOL_RECYCLE")
        self.database_engine_pool_size: int = config.getint("POSTGRES", "DATABASE_ENGINE_POOL_SIZE")
        self.database_engine_max_overflow: int = config.getint("POSTGRES", "DATABASE_ENGINE_MAX_OVERFLOW")
        self.database_engine_pool_ping: bool = config.getboolean("POSTGRES", "DATABASE_ENGINE_POOL_PING")
        self.database_echo: bool = config.getboolean("POSTGRES", "DATABASE_ECHO")

    @property
    def url(self) -> str:
        return (f"{self.database}+{self.driver}://{self.username}:{self.password}@{self.ip}:{self.port}/"
                f"{self.database_name}")


@dataclass
class RedisCfg(CfgBase):
    host: str = os.getenv("REDIS_HOST", config["REDIS"]["HOST"]) if config.has_section("REDIS") else os.getenv("REDIS_HOST", "redis")
    port: int = int(os.getenv("REDIS_PORT", str(config.getint("REDIS", "PORT"))) if config.has_section("REDIS") else os.getenv("REDIS_PORT", "6379"))
    db: int = int(os.getenv("REDIS_DB", str(config.getint("REDIS", "DB"))) if config.has_section("REDIS") else os.getenv("REDIS_DB", "0"))
    password: str = os.getenv("REDIS_PASSWORD", config["REDIS"]["PASSWORD"]) if config.has_section("REDIS") else os.getenv("REDIS_PASSWORD", "")


@dataclass
class UvicornCfg(CfgBase):
    host: str = os.getenv("UVICORN_HOST", config["UVICORN"]["HOST"]) if config.has_section("UVICORN") else os.getenv("UVICORN_HOST", "0.0.0.0")
    port: int = int(os.getenv("UVICORN_PORT", str(config.getint("UVICORN", "PORT"))) if config.has_section("UVICORN") else os.getenv("UVICORN_PORT", "8000"))



uvicorn = UvicornCfg()
redis = RedisCfg()

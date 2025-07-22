from abc import ABC
from dataclasses import asdict, dataclass
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


class CfgBase(ABC):
    dict: callable = asdict


class PostgresCfg(CfgBase):
    def __init__(self):
        self.database: str = config["POSTGRES"]["DATABASE"]
        self.driver: str = config["POSTGRES"]["DRIVER"]
        self.database_name: str = config["POSTGRES"]["DATABASE_NAME"]
        self.username: str = config["POSTGRES"]["USERNAME"]
        self.password: str = config["POSTGRES"]["PASSWORD"]
        self.ip: str = config["POSTGRES"]["IP"]
        self.port: int = config.getint("POSTGRES", "PORT")

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
    host: str = config["REDIS"]["HOST"]
    port: int = config.getint("REDIS", "PORT")
    db: int = config.getint("REDIS", "DB")
    password: str = config["REDIS"]["PASSWORD"]


@dataclass
class UvicornCfg(CfgBase):
    host: str = config["UVICORN"]["HOST"]
    port: int = config.getint("UVICORN", "PORT")



uvicorn = UvicornCfg()
redis = RedisCfg()

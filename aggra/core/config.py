from pydantic import BaseSettings, AnyUrl


class Config(BaseSettings):
    db_uri: AnyUrl
    redis_uri: AnyUrl
    rabbitmq_uri: AnyUrl

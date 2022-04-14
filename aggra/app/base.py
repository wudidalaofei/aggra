from celery import Celery
from fastapi import FastAPI

from aggra import Config
from aggra import logger


class Aggra:
    def __init__(
            self,
            config: Config,
            debug: bool = False
    ):
        self._debug = debug
        self._config = Config

    def setup_celery(self) -> Celery:
        logger.debug("Setting up Celery")
        celery = Celery(
            "aggra",
            config_source=self._config.celery_config,
        )

    def setup_fastapi(self) -> FastAPI:
        pass

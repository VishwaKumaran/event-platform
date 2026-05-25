from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "worker"
    ENVIRONMENT: Literal["local", "dev", "staging", "production"] = "local"

    @computed_field
    @property
    def DEBUG(self) -> bool:
        return self.ENVIRONMENT in ["local", "dev"]

    REDIS_URL: str
    REDIS_STREAM: str = "events.raw"
    GROUP_NAME: str = "workers"
    CONSUMER_NAME: str = "worker-1"


settings = Settings()

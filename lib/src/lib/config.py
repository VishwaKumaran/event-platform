from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "core"
    ENVIRONMENT: Literal["local", "dev", "staging", "production"] = "local"

    @computed_field
    @property
    def DEBUG(self) -> bool:
        return self.ENVIRONMENT in ["local", "dev"]

    POSTGRESQL_URI: str

    REDIS_URL: str
    REDIS_STREAM: str = "events.raw"

from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "backend"
    ENVIRONMENT: Literal["local", "dev", "staging", "production"] = "local"

    @computed_field
    @property
    def DEBUG(self) -> bool:
        return self.ENVIRONMENT in ["local", "dev"]

    API_V1: str = "/api/v1"

    POSTGRESQL_URI: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REDIS_URL: str
    REDIS_STREAM: str = "events.raw"


settings = Settings()

from lib import CoreSettings


class Settings(CoreSettings):
    PROJECT_NAME: str = "backend"
    API_V1: str = "/api/v1"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()

from lib import CoreSettings


class Settings(CoreSettings):
    PROJECT_NAME: str = "worker"
    GROUP_NAME: str = "workers"
    CONSUMER_NAME: str = "worker-1"


settings = Settings()

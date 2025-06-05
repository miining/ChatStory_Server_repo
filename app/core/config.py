from pydantic import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    AI_SERVER_URL: str = "http://localhost:8001"
    PRIVATE_KEY_PATH: Path
    PUBLIC_KEY_PATH: Path
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    MONGO_URL: str
    DB_NAME: str

    # OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"
# 환경 설정 인스턴스
settings = Settings()

# with open(Path(settings.PRIVATE_KEY_PATH), "r") as f:
#     settings.PRIVATE_KEY_PATH = f.read()

# with open(Path(settings.PUBLIC_KEY_PATH), "r") as f:
#     settings.PUBLIC_KEY_PATH = f.read()
    

from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings

load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")

class Settings(BaseSettings):
    DATABASE_POSTGRES_HOST:str


    class config:
        env_file = ".env"


settings = Settings()


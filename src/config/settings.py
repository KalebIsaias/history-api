import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """
    Application settings.
    """

    # FastAPI
    # Debug should be set to False on production
    DEBUG: Optional[bool] = os.getenv("DEBUG") == "True"
    # Title is the name of application
    TITLE: Optional[str] = os.getenv("TITLE")
    # SQLITE connection string
    SQLITE_CONNECTION_STRING: Optional[str] = "sqlite:///database.db"
    # JWT
    SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")
    ALGORITHM: Optional[str] = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    # Origins
    ORIGINS: Optional[str] = os.getenv("ORIGINS")
    # Redis & Celery
    BROKER: Optional[str] = os.getenv("BROKER")
    BACKEND: Optional[str] = os.getenv("BACKEND")
    # PostgreSQL connection string
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_CONNECTION_STRING: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.settings import settings

if settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = settings.SQLITE_CONNECTION_STRING
else:
    SQLALCHEMY_DATABASE_URL = settings.POSTGRES_CONNECTION_STRING

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if settings.DEBUG else {},
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

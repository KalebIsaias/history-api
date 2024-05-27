from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

if settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = settings.SQLITE_CONNECTION_STRING
else:
    SQLALCHEMY_DATABASE_URL = settings.POSTGRES_CONNECTION_STRING

class __DBConnetcionHandler:
  def __init__(self) -> None:
    self.__connection_string = SQLALCHEMY_DATABASE_URL
    self.__engine = None
    self.session = None

  def connect_to_db(self) -> None:
    self.__engine = create_engine(self.__connection_string)

  def get_engine(self):
    return self.__engine
  
  def __enter__(self):
    session_maker = sessionmaker()
    self.session = session_maker(bind=self.__engine)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()

db_connection_handler = __DBConnetcionHandler()
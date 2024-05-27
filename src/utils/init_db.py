from src.models.settings.base import Base
from src.models.settings.connection import db_connection_handler
from src.models.entities.history import History
from src.models.entities.user import User

def create_tables():
  with db_connection_handler as db:
    Base.metadata.create_all(bind=db.get_engine())
    History.metadata.create_all(bind=db.get_engine())
    User.metadata.create_all(bind=db.get_engine())
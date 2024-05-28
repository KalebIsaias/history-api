from src.models.settings.base import Base
from src.models.settings.connection import engine
from src.models.entities.history import History
from src.models.entities.user import User

def create_tables():
  Base.metadata.create_all(bind=engine)
  History.metadata.create_all(bind=engine)
  User.metadata.create_all(bind=engine)
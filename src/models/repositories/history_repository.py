from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.history import History
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class HistoryRepository:
  def create(self, historyInfo: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        history = History(
          title=historyInfo["title"],
          description=historyInfo["description"],
          category=historyInfo["category"],
          content=historyInfo["content"]
        )

        database.session.add(history)
        database.session.commit()

        return historyInfo
      
      except IntegrityError:
        raise Exception("History already exists!")

      except Exception as exception:
        database.session.rollback()
        raise exception
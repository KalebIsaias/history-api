from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.history import History
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class HistoryRepository:
  def get_all(self) -> List[Dict]:
    with db_connection_handler as database:
      try:
        histories = (
          database.session
          .query(History)
          .all()
        )
        return [history for history in histories]

      except NoResultFound:
        raise Exception("No history found!")

      except Exception as exception:
        raise exception
      
  def get_by_id(self, history_id: int) -> Dict:
    with db_connection_handler as database:
      try:
        history = (
          database.session
          .query(History)
          .filter(History.id == history_id)
          .one()
        )

        return history
      
      except NoResultFound:
        return None
      
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
      
  def update(self, history_id: int, historyInfo: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        history = (
          database.session
          .query(History)
          .filter(History.id == history_id)
          .one()
        )

        history.title = historyInfo["title"]
        history.description = historyInfo["description"]
        history.category = historyInfo["category"]
        history.content = historyInfo["content"]

        database.session.commit()

        return historyInfo
      
      except NoResultFound:
        raise Exception("History not found!")
      
      except Exception as exception:
        database.session.rollback()
        raise exception
  
  def delete(self, history_id: int) -> None:
    with db_connection_handler as database:
      try:
        history = (
          database.session
          .query(History)
          .filter(History.id == history_id)
          .one()
        )

        database.session.delete(history)
        database.session.commit()

      except NoResultFound:
        raise Exception("History not found!")
      
      except Exception as exception:
        database.session.rollback()
        raise exception
      
      

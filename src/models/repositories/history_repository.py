from typing import Dict, List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session

from src.models.entities.history import History

class HistoryRepository:
  def __init__(self, session: Session):
    self.session = session
    
  def get_all(self) -> List[Dict]:
    try:
      histories = (
        self.session
        .query(History)
        .all()
      )
      return [history for history in histories]

    except NoResultFound:
      raise Exception("No history found!")

    except Exception as exception:
      raise exception
      
  def get_by_id(self, history_id: int) -> Dict:    
    try:
      history = (
        self.session
        .query(History)
        .filter(History.id == history_id)
        .one()
      )

      return history
    
    except NoResultFound:
      return None
      
  def create(self, historyInfo: Dict) -> Dict:
    try:
      history = History(
        title=historyInfo["title"],
        description=historyInfo["description"],
        category=historyInfo["category"],
        content=historyInfo["content"]
      )

      self.session.add(history)
      self.session.commit()

      return historyInfo
    
    except IntegrityError:
      raise Exception("History already exists!")

    except Exception as exception:
      self.session.rollback()
      raise exception
      
  def update(self, history_id: int, historyInfo: Dict) -> Dict:
    try:
      history = (
        self.session
        .query(History)
        .filter(History.id == history_id)
        .one()
      )

      history.title = historyInfo["title"]
      history.description = historyInfo["description"]
      history.category = historyInfo["category"]
      history.content = historyInfo["content"]

      self.session.commit()

      return historyInfo
    
    except NoResultFound:
      raise Exception("History not found!")
    
    except Exception as exception:
      self.session.rollback()
      raise exception
  
  def delete(self, history_id: int) -> None:
    try:
      history = (
        self.session
        .query(History)
        .filter(History.id == history_id)
        .one()
      )

      self.session.delete(history)
      self.session.commit()

    except NoResultFound:
      raise Exception("History not found!")
    
    except Exception as exception:
      self.session.rollback()
      raise exception
      
      

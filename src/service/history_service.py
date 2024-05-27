from typing import Dict
from src.models.repositories.history_repository import HistoryRepository  

class HistoryService:
  def __init__(self) -> None:
    self.__history_repository = HistoryRepository()

  def get_all(self) -> Dict:
    return self.__history_repository.get_all()
  
  def get_by_id(self, history_id: int) -> Dict:
    return self.__history_repository.get_by_id(history_id)
  
  def create(self, data: Dict) -> Dict:
    return self.__history_repository.create(data)
  
  def update(self, history_id: int, data: Dict) -> Dict:
    return self.__history_repository.update(history_id, data)
  
  def delete(self, history_id: int) -> None:
    return self.__history_repository.delete(history_id)
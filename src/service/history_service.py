from typing import Dict
from src.models.repositories.history_repository import HistoryRepository  

class HistoryService:
  def __init__(self) -> None:
    self.__history_repository = HistoryRepository()

  def create(self, data: Dict) -> Dict:
    return self.__history_repository.create(data)
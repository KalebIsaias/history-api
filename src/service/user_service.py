from typing import Dict
from src.models.repositories.user_repository import UserRepository

class UserService:
  def __init__(self) -> None:
    self.__user_repository = UserRepository()

  def get_all(self) -> Dict:
    return self.__user_repository.get_all()
  
  def get_by_id(self, user_id: int) -> Dict:
    return self.__user_repository.get_by_id(user_id)
  
  def create(self, data: Dict) -> Dict:
    return self.__user_repository.create(data)
  
  def update(self, user_id: int, data: Dict) -> Dict:
    return self.__user_repository.update(user_id, data)
  
  def delete(self, user_id: int) -> None:
    return self.__user_repository.delete(user_id)
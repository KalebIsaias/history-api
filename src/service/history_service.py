from typing import Dict

from sqlalchemy.orm import Session
import google.generativeai as genai

from src.config.settings import settings
from src.models.repositories.history_repository import HistoryRepository  

genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

class HistoryService:
  def __init__(self, session: Session) -> None:
    self.__history_repository = HistoryRepository(session)

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
  
  def enchance_history(self, history_id: int) -> str:
    history = self.__history_repository.get_by_id(history_id)
    
    if not history:
      raise Exception("History not found")
    
    history_content = history.content
    
    response = model.generate_content(
      f"""
      Você é um assistente que melhora histórias, mantendo o sentido e retorna breve textos.
      Aprimore e dê continuidade para essa história:
      {history_content}
      """
    )

    enhanced_history = ""
    for chunk in response:
      enhanced_history += chunk.text
      enhanced_history += "\n"
    
    return {
      "history": history_content,
      "enhanced_history": enhanced_history
    }
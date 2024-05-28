from typing import Dict
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from src.models.repositories.user_repository import UserRepository
from src.auth.security import get_password_hash, pwd_context, create_access_token
from src.config.settings import settings

class UserService:
  def __init__(self, session: Session) -> None:
    self.__user_repository = UserRepository(session)
  
  def get_all(self) -> Dict:
    return self.__user_repository.get_all()
  
  def get_by_id(self, user_id: int) -> Dict:
    return self.__user_repository.get_by_id(user_id)
  
  def create(self, data: Dict) -> Dict:
    hashed_password = get_password_hash(data["password"])
    return self.__user_repository.create(data, hashed_password)
  
  def update(self, user_id: int, data: Dict) -> Dict:
    return self.__user_repository.update(user_id, data)
  
  def delete(self, user_id: int) -> None:
    return self.__user_repository.delete(user_id)
  
  def login(self, data: OAuth2PasswordRequestForm):
    user = self.__user_repository.get_user_by_username(data.username)

    if not user or not pwd_context.verify(data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}

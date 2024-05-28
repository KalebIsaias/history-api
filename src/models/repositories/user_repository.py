from typing import Dict, List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session

from src.models.entities.user import User

class UserRepository:
  def __init__(self, session: Session):
    self.session = session

  def get_all(self) -> List[Dict]:
      try:
        users = (
          self.session
          .query(User)
          .all()
        )
        return [user for user in users]

      except NoResultFound:
        raise Exception("No user found!")

      except Exception as exception:
        raise exception
      
  def get_by_id(self, user_id: int) -> Dict:
      try:
        user = (
          self.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        return user
      
      except NoResultFound:
        return None
  
  def get_user_by_username(self, username: str) -> Dict:
    # try:
    #   user = (
    #     self.session
    #     .query(User)
    #     .filter(User.username == username)
    #     .first()
    #   )

    #   return user
        
    # except NoResultFound:
    #   return None
    return self.session.query(User).filter(User.username == username).first()

  def create(self, userInfo: Dict, hashed_password: str) -> Dict:
      try:
        user = User(
          username=userInfo["username"],
          password=hashed_password
        )

        self.session.add(user)
        self.session.commit()

        return userInfo
      
      except IntegrityError:
        raise Exception("User already exists!")

      except Exception as exception:
        self.session.rollback()
        raise exception
      
  def update(self, user_id: int, userInfo: Dict) -> Dict:
      try:
        user = (
          self.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        user.username = userInfo["username"]
        user.password = userInfo["password"]

        self.session.commit()

        return userInfo
      
      except NoResultFound:
        return None

      except Exception as exception:
        self.session.rollback()
        raise exception
      
  def delete(self, user_id: int) -> None:
      try:
        user = (
          self.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        self.session.delete(user)
        self.session.commit()
      
      except NoResultFound:
        return None

      except Exception as exception:
        self.session.rollback()
        raise exception
  
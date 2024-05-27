from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.user import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class UserRepository:
  def get_all(self) -> List[Dict]:
    with db_connection_handler as database:
      try:
        users = (
          database.session
          .query(User)
          .all()
        )
        return [user for user in users]

      except NoResultFound:
        raise Exception("No user found!")

      except Exception as exception:
        raise exception
      
  def get_by_id(self, user_id: int) -> Dict:
    with db_connection_handler as database:
      try:
        user = (
          database.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        return user
      
      except NoResultFound:
        return None
  
  def create(self, userInfo: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        user = User(
          username=userInfo["username"],
          password=userInfo["password"]
        )

        database.session.add(user)
        database.session.commit()

        return userInfo
      
      except IntegrityError:
        raise Exception("User already exists!")

      except Exception as exception:
        database.session.rollback()
        raise exception
      
  def update(self, user_id: int, userInfo: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        user = (
          database.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        user.username = userInfo["username"]
        user.password = userInfo["password"]

        database.session.commit()

        return userInfo
      
      except NoResultFound:
        return None

      except Exception as exception:
        database.session.rollback()
        raise exception
      
  def delete(self, user_id: int) -> None:
    with db_connection_handler as database:
      try:
        user = (
          database.session
          .query(User)
          .filter(User.id == user_id)
          .one()
        )

        database.session.delete(user)
        database.session.commit()
      
      except NoResultFound:
        return None

      except Exception as exception:
        database.session.rollback()
        raise exception
from sqlalchemy import Column, Integer, String
from src.models.settings.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return "<User id={} username={}>".format(
            self.id,
            self.username
        )
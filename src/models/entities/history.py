from sqlalchemy import Column, Integer, String, Text
from src.models.settings.base import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(255), nullable=False)
    content = Column(Text)

    def __repr__(self):
        return "<History id={} title={} description={} category={} content={}>".format(
            self.id,
            self.title,
            self.description,
            self.category,
            self.content
        )
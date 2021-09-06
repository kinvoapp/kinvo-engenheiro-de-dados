from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Text
from sqlalchemy.orm import relationship

from . import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    link = Column(Text, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False)

    entities = relationship("Entity", back_populates="news")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    entity = Column(String, nullable=False)

    news_id = Column(Integer, ForeignKey("news.id"))

    news = relationship("News", back_populates="entities")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

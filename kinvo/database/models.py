from sqlalchemy import Column, Integer, DateTime, Text

from . import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    link = Column(Text, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    pub_date = Column(DateTime, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns
                if not str(c.name) == 'id'}

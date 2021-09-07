from typing import List

from kinvo.database.schemas import News


from . import models, SessionLocal


def get_news(skip: int = 0, limit: int = 5) -> List[models.News]:
    with SessionLocal() as db:
        result = db.query(models.News).offset(skip).limit(limit).all()

    return result


def create_news(news: News) -> models.News:
    db_news = models.News(**news.dict())

    with SessionLocal() as db:
        db.add(db_news)
        db.commit()
        db.refresh(db_news)

    return db_news

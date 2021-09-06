from typing import List

from kinvo.database.schemas import News, Entity


from . import models, SessionLocal


def count_news() -> int:
    with SessionLocal() as db:
        result = db.query(models.News).count()

    return result


def get_news_by_link(link: str) -> models.News:
    with SessionLocal() as db:
        result = db.query(models.News).filter(models.News.link == link).first()

    return result


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


def count_entities() -> int:
    with SessionLocal() as db:
        result = db.query(models.Feature).count()

    return result


def get_entity_by_news_id(news_id: int) -> models.Entity:
    with SessionLocal() as db:
        result = db.query(models.Entity).\
            filter(models.Entity.news_id == news_id).first()

    return result


def get_entities() -> List[models.Entity]:
    with SessionLocal() as db:
        result = db.query(models.Entity).\
            with_entities(models.Entity.breed_id).all()

    return result


def create_entity(feature: Entity) -> models.Entity:
    db_entity = models.Entity(**feature.dict())

    with SessionLocal() as db:
        db.add(db_entity)
        db.commit()
        db.refresh(db_entity)

    return db_entity

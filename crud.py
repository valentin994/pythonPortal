from sqlalchemy.orm import Session

import models
import schemas


def create_post(db: Session, post: schemas.CreatePost):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, limit: int, page: int):
    return db.query(models.Post).slice(page * limit, limit).all()

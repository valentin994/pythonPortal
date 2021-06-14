from sqlalchemy.orm import Session
import models
import schemas


def create_post(db: Session, post: schemas.Post):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

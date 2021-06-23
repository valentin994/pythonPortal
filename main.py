from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/post/", response_model=schemas.CreatePost)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post.__dict__


@app.get("/post/{post_id}", response_model=schemas.GetPost)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    return db_post.__dict__


@app.get("/posts/")
def get_posts(page: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    db_posts = crud.get_posts(db, limit, page)
    return db_posts

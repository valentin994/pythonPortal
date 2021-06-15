from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

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
def get_post(post_id: int, db: Session = Depends((get_db))):
    db_post = crud.get_post(db, post_id)
    print(db_post)
    return db_post.__dict__
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


@app.post("/post/", response_model=schemas.Post)
def create_post(post: schemas.Post, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post

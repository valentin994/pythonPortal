from typing import List
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    desc: str
    list_of_contents: List[str]
    content: List[str]
    tags: List[str]

    class Config:
        orm_mode: True

from typing import List
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    desc: str
    list_of_contents: List[str]
    content: List[str]
    tags: List[str]

    class Config:
        orm_mode: True
        schema_extra={
            "example":{
                "title": "Variables",
                "desc": "This post is about variables",
                "list_of_contents": [
                    "String",
                    "Integer",
                    "Float"
                ],
                "content": ["First section", "Second section", "Third section"],
                "tags": ["begginer", "variables"]
            }
        }

from sqlalchemy import Table, Column, Integer, String, MetaData, ARRAY
from database import Base


class Post(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    desc = Column(String)
    list_of_contents = Column(ARRAY(String))
    content = Column(ARRAY(String))
    tags = Column(ARRAY(String))

    def __repr__(self):
        return f"Post ID: {self.id}, Post Title: {self.title}"

from database import engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ARRAY

meta = MetaData()
posts = Table(
    'posts', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('desc', String, nullable=False),
    Column('list_of_contents', ARRAY(String), nullable=False),
    Column('content', ARRAY(String), nullable=False),
    Column('tags', ARRAY(String), nullable=False)
)

meta.create_all(engine)
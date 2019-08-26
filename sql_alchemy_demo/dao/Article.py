from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text
from sql_alchemy_demo.db.db_commons import meta

'''first entity with pk: article'''
article = Table(
    'article', meta,
    Column('article_id', Integer, primary_key=True),
    Column('title', String),
    Column('content', Text),
    Column('post_user', String),
    Column('votes', Integer),
    Column('post_time', DateTime),
    Column('score', Float)
)

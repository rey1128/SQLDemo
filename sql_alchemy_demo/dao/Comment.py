from sqlalchemy import Table, Column, Integer, String, Text
from sql_alchemy_demo.db.db_commons import meta

'''another entity comment
connect with entity with article_id, but not using fk
'''
comment = Table(
    'comment', meta,
    Column('comment_id', Integer, primary_key=True),
    Column('post_user', String),
    Column('content', Text),
    Column('article_id', Integer)
)

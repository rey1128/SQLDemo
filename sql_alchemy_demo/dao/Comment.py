from sqlalchemy import Table, Column, Integer, Text, DateTime, ForeignKey
from sql_alchemy_demo.db.db_commons import meta
import datetime

'''another entity comment
connect with entity with article_id, but not using fk
'''
comment = Table(
    'comment', meta,
    Column('comment_id', Integer, primary_key=True),
    Column('post_user_id', Integer, ForeignKey('postuser.user_id'), nullable=False),
    Column('content', Text),
    Column('post_time', DateTime, default=datetime.datetime.utcnow()),
    Column('article_id', Integer, ForeignKey('article.article_id'), nullable=False)
)

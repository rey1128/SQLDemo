from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Text, ForeignKey
from sql_alchemy_demo.db.db_commons import meta
from commons.common_constants import *
import datetime

'''first entity with pk: article'''
article = Table(
    'article', meta,
    Column('article_id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('content', Text),
    Column('post_user_id', Integer, ForeignKey('postuser.user_id'), nullable=False),
    Column('votes', Integer, default=1),
    Column('post_time', DateTime, default=datetime.datetime.utcnow()),
    Column('update_time', DateTime, default=datetime.datetime.utcnow()),
    Column('score', Float, default=VOTE_SCORE)
)

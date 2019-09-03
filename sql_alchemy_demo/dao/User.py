from sqlalchemy import Table, Column, Integer, String, DateTime, Float
from sql_alchemy_demo.db.db_commons import meta
from commons.common_constants import *
import datetime

user = Table(
    'postuser', meta,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String, nullable=False, unique=True),
    Column('reg_time', DateTime, default=datetime.datetime.utcnow()),
    Column('score', Float, default=USER_SCORE)
)

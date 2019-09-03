from sql_alchemy_demo.dao.User import user
from sql_alchemy_demo.db.db_commons import *


def create_user(user_name):
    insert = user.insert().values(user_name=user_name)
    rt = execute_stmt(insert, db_engine)

    return rt.inserted_primary_key[0]


def delete_user_by_id(u_id):
    dele = user.delete().where(user.c.user_id == u_id)
    execute_stmt(dele, db_engine)
    pass


def get_all_users():
    sel = user.select().order_by('user_id')
    rt = execute_stmt(sel, db_engine)
    return rt


def get_user_by_id(u_id):
    sel = user.select().where(user.c.user_id == u_id)
    rt = execute_stmt(sel, db_engine)
    return rt

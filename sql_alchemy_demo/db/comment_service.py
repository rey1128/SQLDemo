from sql_alchemy_demo.dao.Comment import comment
from sql_alchemy_demo.dao.Article import article
from sqlalchemy.sql import select
from sql_alchemy_demo.db.db_commons import *


def create_comment_for_article(user, cont, a_id):
    ins = comment.insert().values(post_user=user, content=cont, article_id=a_id)
    execute_stmt(ins, db_engine)
    pass


def get_comment_by_id(c_id):
    select_stmt = comment.select().where(comment.c.comment_id == c_id)
    rs = execute_stmt(select_stmt, db_engine)
    return rs


def get_comment_by_article_id(a_id):
    select_stmt = comment.select().where(comment.c.article_id == a_id)
    rs = execute_stmt(select_stmt, db_engine)
    return rs


def get_all_active_comments():
    join = select([article, comment]).where(article.c.article_id == comment.c.article_id)
    rs = execute_stmt(join, db_engine)
    return rs


def get_all_comments():
    select_stmt = comment.select()
    rs = execute_stmt(select_stmt, db_engine)
    return rs

from sql_alchemy_demo.dao.Article import article
from sql_alchemy_demo.db.db_commons import *
import datetime


def create_article(title, post_user_id, cont):
    ins = article.insert().values(title=title, post_user_id=post_user_id, content=cont)
    execute_stmt(ins, db_engine)
    pass


def delete_all_articles():
    dele = article.delete()
    execute_stmt(dele, db_engine)
    pass


def delete_article_by_id(a_id):
    dele = article.delete().where(article.c.article_id == a_id)
    execute_stmt(dele, db_engine)
    pass


def update_article_by_id(a_id, title, cont):
    upd = article.update().where(article.c.article_id == a_id).values(title=title, content=cont,
                                                                      update_time=datetime.datetime.utcnow())
    execute_stmt(upd, db_engine)
    pass


def get_all_articles():
    sel = article.select().order_by('article_id')
    rt = execute_stmt(sel, db_engine)
    return rt


def get_article_by_id(a_id):
    sel = article.select().where(article.c.article_id == a_id)
    rt = execute_stmt(sel, db_engine)
    return rt


def get_articles_by_title(a_title):
    sel = article.select().where(article.c.title == a_title).order_by('article_id')
    rt = execute_stmt(sel, db_engine)
    return rt


def get_articles_by_user(user_id):
    sel = article.select().where(article.c.post_user_id == user_id).order_by('article_id')
    rt = execute_stmt(sel)
    return rt

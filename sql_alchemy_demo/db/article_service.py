from sql_alchemy_demo.dao.Article import article
from sql_alchemy_demo.db.db_commons import *
from datetime import datetime
from commons.common_constants import *


def create_article(title, post_user, cont):
    ins = article.insert().values(title=title, post_user=post_user, content=cont, votes=1,
                                  post_time=datetime.now(),
                                  score=VOTE_SCORE)
    execute_stmt(ins, db_engine)
    pass


def delete_all_articles():
    dele = article.delete()
    execute_stmt(dele, db_engine)
    pass


def delete_article_by_id(a_id):
    dele = article.delete().where(article.c.article_id== a_id)
    execute_stmt(dele, db_engine)
    pass


def update_article_by_id(a_id, title, cont):
    upd = article.update().where(article.c.article_id == a_id).values(title=title, content=cont)
    execute_stmt(upd, db_engine)
    pass


def get_all_articles():
    sel = article.select()
    rt = execute_stmt(sel, db_engine)
    return rt


def get_article_by_id(a_id):
    sel = article.select().where(article.c.article_id == a_id)
    rt = execute_stmt(sel, db_engine)
    return rt


def get_article_by_title(a_title):
    sel = article.select().where(article.c.title == a_title)
    rt = execute_stmt(sel, db_engine)
    return rt

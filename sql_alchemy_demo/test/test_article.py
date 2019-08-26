import unittest

import sql_alchemy_demo.db.article_service as srv
import sql_alchemy_demo.db.db_commons as db_commons
import datetime

from commons.common_constants import *


class TestArticle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('init')
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.create_all(db_engine)
        srv.create_article('init_article', 'init_user', 'this is an article for initialization')
        srv.create_article('article_for_deletion', 'init_user', 'this is an article for initialization')
        pass

    @classmethod
    def tearDownClass(cls):
        print('clean up')
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.drop_all(db_engine)
        pass

    def test_get_article_by_id(self):
        rt = srv.get_article_by_id(a_id=1)
        article = rt.fetchone()
        self.assertIsNotNone(article)
        self.assertEqual('init_article', article.title)
        pass

    def test_get_article_by_title(self):
        rt = srv.get_article_by_title('no_such_article')
        article = rt.fetchone()
        self.assertIsNone(article)
        pass

    def test_create_article(self):
        title = 'test_article'
        user = 'test_user'
        cont = 'this is a test article'

        rt = srv.get_article_by_title(title)
        article = rt.fetchone()
        self.assertIsNone(article)

        srv.create_article(title=title, post_user=user, cont=cont)

        rt = srv.get_article_by_title(title)
        article = rt.fetchone()
        self.assertIsNotNone(article)
        self.assertEqual(title, article.title)
        self.assertEqual(user, article.post_user)
        self.assertEqual(cont, article.content)
        self.assertEqual(1, article.votes)
        self.assertEqual(VOTE_SCORE, article.score)
        self.assertIsNotNone(article.post_time)

        pass

    def test_delete_article_by_id(self):
        rt = srv.get_article_by_id(2)
        article = rt.fetchone()
        self.assertIsNotNone(article)

        srv.delete_article_by_id(2)

        rt = srv.get_article_by_id(2)
        article = rt.fetchone()
        self.assertIsNone(article)
        pass

    def test_free_sql(self):
        now_time = datetime.datetime.now()
        sql = "select * from article where post_time < '%s'" % now_time
        rt = db_commons.free_stmt(sql)
        article = rt.fetchone()
        self.assertIsNotNone(article)
        pass

    pass

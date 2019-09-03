import unittest
import sql_alchemy_demo.db.article_service as article_srv
import sql_alchemy_demo.db.user_service as user_srv
import sql_alchemy_demo.db.comment_service as comment_srv


class TestCommnet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('init')
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.create_all(db_engine)
        user_id1 = user_srv.create_user('test_user_1')
        user_id2 = user_srv.create_user('test_user_2')
        user_id3 = user_srv.create_user('test_user_3')

        article_srv.create_article('article_1', user_id1, 'this is an article for testing')
        article_srv.create_article('article_2', user_id1, 'this is an article for testing2')
        article_srv.create_article('article_3', user_id1, 'this is an article for testing3')

        comment_srv.create_comment_for_article(user_id1, 'comment for article_1', 1)
        comment_srv.create_comment_for_article(user_id2, 'comment for article_1', 1)
        comment_srv.create_comment_for_article(user_id1, 'comment for article_1', 1)

        comment_srv.create_comment_for_article(user_id1, 'comment for article_2', 2)
        comment_srv.create_comment_for_article(user_id3, 'comment for article_2', 2)

        pass

    @classmethod
    def tearDownClass(cls):
        print('clean up')
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.drop_all(db_engine)
        pass

    def test_create_comment(self):
        print('this is a test for creating comment')

        pass

    def test_get_comment_by_article_id(self):
        rs = comment_srv.get_comments_by_article_id(1)
        comments = list(rs.fetchall())
        self.assertEqual(3, len(comments))

        rs = comment_srv.get_comments_by_article_id(2)
        comments = list(rs.fetchall())
        self.assertEqual(2, len(comments))

        rs = comment_srv.get_comments_by_article_id(3)
        self.assertIsNone(rs.fetchone())

        pass

    def test_comment_by_id(self):
        rs = comment_srv.get_comment_by_id(1)
        comment = rs.fetchone()
        self.assertIsNotNone(comment)
        self.assertEqual(1, comment.post_user_id)
        self.assertEqual('comment for article_1', comment.content)
        self.assertEqual(1, comment.article_id)
        pass

    def test_get_all_comments(self):
        rs = comment_srv.get_all_comments()
        comments = list(rs.fetchall())
        last_comment = comments[-1]
        self.assertEqual(5, len(comments))
        self.assertEqual(2, last_comment.article_id)
        self.assertEqual(3, last_comment.post_user_id)
        self.assertEqual('comment for article_2', last_comment.content)
        pass

    # def test_get_active_commnet(self):
    #     rs = comment_srv.get_all_active_comments()
    #     article_comments = list(rs.fetchall())
    #     self.assertEqual(5, len(article_comments))
    #     pass

import unittest
import sql_alchemy_demo.db.user_service as srv


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.create_all(db_engine)
        pass

    @classmethod
    def tearDownClass(cls):
        from sql_alchemy_demo.db.db_commons import meta, db_engine
        meta.drop_all(db_engine)
        pass

    def test_create_user(self):
        rt = srv.get_all_users()
        self.assertIsNone(rt.fetchone())
        srv.create_user('u1')
        rt = srv.get_user_by_id(1)
        user = rt.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual('u1', user.user_name)

        pass

    def test_get_all_users(self):
        rt = srv.get_all_users()
        self.assertIsNotNone(rt)
        pass

    def test_delete_user_by_id(self):
        rt = srv.get_user_by_id(1)
        self.assertIsNotNone(rt.fetchone())

        srv.delete_user_by_id(1)
        rt = srv.get_user_by_id(1)
        self.assertIsNone(rt.fetchone())
        pass

    pass

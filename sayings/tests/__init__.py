# import unittest
# import transaction
#
# from pyramid import testing
#
# from .models.db_session import DBSession
#
#
# class TestMyViewSuccessCondition(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('mysql://root:root@127.0.0.1/sayings_development?charset=utf8&use_unicode=0')
#         from models.db_session import DBSession
#         from models.db_session import Base
#         DBSession.configure(bind=engine)
#         Base.metadata.create_all(engine)
#         with transaction.manager:
#             pass
#
#     def tearDown(self):
#         DBSession.remove()
#         testing.tearDown()
#
#     def test_passing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'sayings')
#
#
# class TestMyViewFailureCondition(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#         from sqlalchemy import create_engine
#         engine = create_engine('mysql://root:root@127.0.0.1/sayings_development?charset=utf8&use_unicode=0')
#         from models.db_session import DBSession
#         from models.db_session import Base
#         DBSession.configure(bind=engine)
#
#     def tearDown(self):
#         DBSession.remove()
#         testing.tearDown()
#
#     def test_failing_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
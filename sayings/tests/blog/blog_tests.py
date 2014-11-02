import unittest
import transaction

from pyramid import testing
from ...models.db_session import DBSession
from ...models.base import Base


class BlogTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('mysql://root:root@127.0.0.1/sayings_development?charset=utf8&use_unicode=0')
        DBSession.configure(bind=engine)
        # Base.metadata.create_all(engine)
        # with transaction.manager:
        #     pass

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_blog_index(self):
        from sayings.views.blog.blog import Blog
        request = testing.DummyRequest()
        blog = Blog(request)
        blog_index = blog.index()
        self.assertEqual(blog_index['project'], 'Blog')
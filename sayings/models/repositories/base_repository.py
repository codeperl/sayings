from ..db_session import DBSession
import transaction


class BaseRepository(object):
    def __init__(self):
        self.db_session = DBSession

    def commit(self):
        self.db_session.flush()
        transaction.commit()

    def rollback(self):
        self.db_session.rollback()
from .base_repository import BaseRepository
from ..entities.page import Page
from webhelpers.text import urlify
from datetime import datetime


class PageRepository(BaseRepository):
    def __init__(self):
        super(PageRepository, self).__init__()
        self.page = Page

    def find_first_by_name(self, name):
        first = self.db_session.query(self.page).filter(self.page.name == str(name)).first()
        return first

    def find_one_by_id(self, id):
        page = self.db_session.query(self.page).filter(self.page.id == id).first()
        return page

    def add(self, page):
        if page.name:
            page.alias = urlify(page.name)

        page.created_at = datetime.now()

        self.db_session.add(page)
        self.commit()

        return page

    def update(self, page):
        if page.name:
            page.alias = urlify(page.name)

        page.updated_at = datetime.now()

        self.commit()

        return page

    def delete(self, page):
        try:
            self.db_session.delete(page)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.page).all()
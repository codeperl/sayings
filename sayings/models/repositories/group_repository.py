from ..entities.group import Group
from .base_repository import BaseRepository
from webhelpers.text import urlify
from datetime import datetime


class GroupRepository(BaseRepository):
    def __init__(self):
        super(GroupRepository, self).__init__()
        self.group = Group

    def find_first_by_name(self, name):
        first = self.db_session.query(self.group).filter(self.group.name == str(name)).first()
        return first

    def find_one_by_id(self, id):
        group = self.db_session.query(self.group).filter(self.group.id == id).first()
        return group

    def add(self, group):
        if group.name:
            group.alias = urlify(group.name)

        group.created_at = datetime.now()

        self.db_session.add(group)
        self.commit()

        return group

    def update(self, group):
        if group.name:
            group.alias = urlify(group.name)

        group.updated_at = datetime.now()

        self.commit()

        return group

    def delete(self, group):
        try:
            self.db_session.delete(group)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.group).all()

from ..entities.role import Role
from .base_repository import BaseRepository
from webhelpers.text import urlify
from datetime import datetime


class RoleRepository(BaseRepository):
    def __init__(self):
        super(RoleRepository, self).__init__()
        self.role = Role

    def find_first_by_name(self, name):
        first = self.db_session.query(self.role).filter(self.role.name == str(name)).first()
        return first

    def find_one_by_id(self, id):
        role = self.db_session.query(self.role).filter(self.role.id == id).first()
        return role

    def add(self, role):
        if role.name:
            role.alias = urlify(role.name)

        role.created_at = datetime.now()

        self.db_session.add(role)
        self.commit()

        return role

    def update(self, role):
        if role.name:
            role.alias = urlify(role.name)

        role.updated_at = datetime.now()

        self.commit()

        return role

    def delete(self, role):
        try:
            self.db_session.delete(role)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.role).all()
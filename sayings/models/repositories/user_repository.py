from ..entities.user import User
from .base_repository import BaseRepository
from webhelpers.text import urlify
from datetime import datetime


class UserRepository(BaseRepository):
    def __init__(self):
        super(UserRepository, self).__init__()
        self.user = User

    def find_first_by_email(self, email):
        first = self.db_session.query(self.user).filter(self.user.email == str(email)).first()
        return first

    def find_one_by_id(self, id):
        user = self.db_session.query(self.user).filter(self.user.id == id).first()
        return user

    def add(self, user):
        if user.email:
            user.alias = urlify(user.email)

        user.created_at = datetime.now()

        self.db_session.add(user)
        self.commit()

        return user

    def update(self, user):
        if user.email:
            user.alias = urlify(user.email)

        user.updated_at = datetime.now()

        self.commit()

        return user

    def delete(self, user):
        try:
            self.db_session.delete(user)
            self.commit()
            return True
        except:
            self.rollback()
            return False

    def all(self):
        return self.db_session.query(self.user).all()
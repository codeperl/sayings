from ..entities.profile import Profile
from .base_repository import BaseRepository


class ProfileRepository(BaseRepository):
    def __init__(self):
        super(ProfileRepository, self).__init__()
        self.profile = Profile

    def all(self):
        return self.db_session.query(self.profile).all()
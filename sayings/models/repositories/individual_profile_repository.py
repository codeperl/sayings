from ..entities.individual_profile import IndividualProfile
from .base_repository import BaseRepository


class IndividualProfileRepository(BaseRepository):
    def __init__(self):
        super(IndividualProfileRepository, self).__init__()
        self.individual_profile = IndividualProfile

    def all(self):
        return self.db_session.query(self.individual_profile).all()
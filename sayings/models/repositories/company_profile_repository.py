from ..entities.company_profile import CompanyProfile
from .base_repository import BaseRepository


class CompanyProfileRepository(BaseRepository):
    def __init__(self):
        super(CompanyProfileRepository, self).__init__()
        self.company_profile = CompanyProfile

    def all(self):
        return self.db_session.query(self.company_profile).all()
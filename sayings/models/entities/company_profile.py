from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from ..base import Base
from sqlalchemy.orm import relationship, backref
from sayings.models.entities.profile import Profile


class CompanyProfile(Profile):
    __tablename__ = 'company_profiles'
    __mapper_args__ = {'polymorphic_identity': 'company'}
    id = Column(Integer, ForeignKey('profiles.id'), primary_key=True)
    demo_column = Column(String(50), index=True)
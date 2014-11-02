from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from ..base import Base
from sqlalchemy.orm import relationship, backref
from sayings.models.entities.profile import Profile


class IndividualProfile(Profile):
    __tablename__ = 'individual_profiles'
    __mapper_args__ = {'polymorphic_identity': 'individual'}
    id = Column(Integer, ForeignKey('profiles.id'), primary_key=True)
    demo_column = Column(String(50), index=True)
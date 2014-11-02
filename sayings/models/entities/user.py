from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from ..base import Base
from sqlalchemy.orm import relationship, backref
from sayings.models.entities.profile import Profile


class User(Base):
    """
    Class User.
    It will contain all users.
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, index=True, unique=True)
    password = Column(String(155), nullable=False)
    profiles = relationship("Profile")
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
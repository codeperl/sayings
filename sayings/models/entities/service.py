from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean
)
from ..base import Base
from sqlalchemy.orm import relationship, backref


class Service(Base):
    """
    Class Service.
    It will contain all services.
    """

    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    alias = Column(String(155), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    profile_id = Column(Integer, ForeignKey('profiles.id'), index=True)
    profile = relationship('Profile', backref=backref('services', lazy='dynamic'))
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
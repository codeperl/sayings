from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship, backref
from ..base import Base
from sayings.models.entities.product import Product
from sayings.models.entities.service import Service


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # products = relationship("Product", cascade="all, delete, delete-orphan")
    # services = relationship("Service", cascade="all, delete, delete-orphan")
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    type = Column(String(200), nullable=False)
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'profile',
        'with_polymorphic': '*'
    }
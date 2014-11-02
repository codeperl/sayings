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


class Product(Base):
    """
    Class Product.
    It will contain all products.
    """

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    alias = Column(String(155), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    profile_id = Column(Integer, ForeignKey('profiles.id'), index=True)
    profile = relationship('Profile', backref=backref('products', lazy='dynamic'))
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
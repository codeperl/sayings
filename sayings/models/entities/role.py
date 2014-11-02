from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)
from ..base import Base


class Role(Base):
    """
    Class Role.
    It will contain all roles.
    """

    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True, unique=True)
    alias = Column(String(155), nullable=False, unique=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
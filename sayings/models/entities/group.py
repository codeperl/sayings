from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)
from ..base import Base
from sqlalchemy.orm import relationship
from sayings.models.entities.group_user import GroupUser
from sayings.models.entities.group_role import GroupRole


class Group(Base):
    """
    Class Group.
    It will contain all groups.
    """

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True, unique=True)
    alias = Column(String(155), nullable=False, unique=True)
    users = relationship("GroupUser", backref="group")
    roles = relationship("GroupRole", backref="role")
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship, backref
from ..base import Base
from sayings.models.entities.user import User


class GroupUser(Base):
    __tablename__ = 'groups_users'
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    active = Column(Boolean, default=False)
    guser = relationship("User", backref="group_user_assocs")
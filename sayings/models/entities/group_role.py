from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship, backref
from ..base import Base
from sayings.models.entities.role import Role


class GroupRole(Base):
    __tablename__ = 'groups_roles'
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    active = Column(Boolean, default=False)
    grole = relationship("Role", backref="group_role_assocs")
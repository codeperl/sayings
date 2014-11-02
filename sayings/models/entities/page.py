from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)
from ..base import Base


class Page(Base):
    """
    Class Page.
    It will contain all pages.
    """

    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    alias = Column(String(155), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
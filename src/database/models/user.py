import uuid
from sqlalchemy.orm import Mapped

from sqlalchemy import text, types, String, Boolean
from .base import Base, uuid


class User(Base):
    guid: Mapped[uuid]
    email: Mapped[str]
    price: Mapped[int]
    count: Mapped[int]

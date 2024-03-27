import uuid
from typing import Annotated

from sqlalchemy import (
    DateTime,
    Identity,
    Integer,
    LargeBinary,
    String,
    func,
)
from sqlalchemy import text, types
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """table name like class name"""
        return f"{cls.__name__.lower()}"


class CustomType:
    # required
    email_type = Annotated[str, mapped_column(String(250))]
    password_type = Annotated[LargeBinary, mapped_column(LargeBinary)]

    # optional
    id_type = Annotated[int, mapped_column(Integer, Identity(), primary_key=True)]
    username_type = Annotated[str, mapped_column(String(32), nullable=False)]
    role_type = Annotated[str, mapped_column(String(10), default="user")]
    created_at_type = Annotated[
        DateTime,
        mapped_column(DateTime, server_default=func.now(), nullable=False),
    ]
    updated_at_type = Annotated[
        DateTime,
        mapped_column("updated_at", DateTime, onupdate=func.now(), nullable=True),
    ]

    # not used
    uuid = Annotated[
        uuid.UUID,
        mapped_column(
            types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
        ),
    ]

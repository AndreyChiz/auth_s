from sqlalchemy.orm import DeclarativeBase, declared_attr
from typing import Annotated
import uuid
from sqlalchemy import text, types
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"



uuid = Annotated[uuid.UUID, mapped_column(
        types.Uuid,
        primary_key=True,
        init=False,
        server_default=text("gen_random_uuid()")
    )
]
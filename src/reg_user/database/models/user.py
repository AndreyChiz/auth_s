from sqlalchemy.orm import Mapped

from .base import Base, CustomType


class User(Base):
    id: Mapped[CustomType.id_type]
    username: Mapped[CustomType.username_type]
    password: Mapped[CustomType.password_type]
    role: Mapped[CustomType.role_type]
    email: Mapped[CustomType.email_type]
    created_at: Mapped[CustomType.created_at_type]
    updated_at: Mapped[CustomType.updated_at_type]
# random_uuid = uuid.uuid4()
# cs = UserRQST(id=random_uuid, email="asd@ssfe.ds")
# print(cs.id)

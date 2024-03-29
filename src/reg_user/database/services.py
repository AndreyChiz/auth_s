import datetime
from typing import Any

from sqlalchemy import select, insert

from .manager import fetch_one
from .models import User
from .utils import hash_password


async def get_user_by_email(email: str):
    select_query = select(User).where(User.email == email)

    return await fetch_one(select_query)


async def get_user_by_username(username: str):

    select_query = select(User).where(User.username == username)
    return await fetch_one(select_query)


async def write_user(email: str, password: str, username: str) -> dict[str, Any] | None:
    insert_query = (
        insert(User)
        .values(
            {
                "username": username,
                "email": email,
                "password": password,
                # "created_at": datetime.datetime.now(datetime.UTC),  # TODO check
            }
        )
        .returning(User)  # TODO check
    )
    return await fetch_one(insert_query)

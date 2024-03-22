from .schemas import UserAuth
from .database import get_user_by_email, get_user_by_username
from .exceptions import EmailTaken, UsernameTaken


async def check_unique_user_data(user_auth_data: UserAuth):
    """Check existing user with equal data (before creating and writing user data to database)"""
    if await get_user_by_email(user_auth_data.email):
        raise EmailTaken()
    if await get_user_by_username(user_auth_data.username):
        raise UsernameTaken()
    return user_auth_data


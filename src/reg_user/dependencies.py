from .schemas import UserAuth
from .database import get_user_by_email, get_user_by_username
from .exceptions import UserAlreadyExist, UserNotExist
from .repos import User


async def is_user_not_exist(user_auth_data: UserAuth):
    """Check absence user with equal data (before creating and writing user data to database)"""
    user_by_name = User(username=user_auth_data.username)
    user_by_email = User(email=user_auth_data.email)
    if (
        await user_by_name.load_data_to_instance()
        or await user_by_email.load_data_to_instance()
    ):
        raise UserAlreadyExist
    return user_auth_data

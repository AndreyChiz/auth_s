from .schemas import UserAuth
from .repos import User
from .utils import hash_password, check_password


async def create_user(user_auth_data: UserAuth):
    """Create new user"""
    user = User(**user_auth_data.model_dump())
    user.password = hash_password(user.password)
    return await user.create_user()


async def login_user(user_credentials: UserAuth):
    user = User(**user_credentials.model_dump())
    request_password = user.password  # secretStr !!!
    await user.load_data_to_instance()
    print(check_password(request_password, user.password))

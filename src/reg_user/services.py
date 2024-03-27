from .schemas import UserAuth
from .repos import User

async def create_user(user_auth_data: UserAuth):
    """Create new user"""
    return await User().create_user(**user_auth_data.model_dump())


async def get_user():
    pass    

from .schemas import UserAuth
from .repos import User

async def create_user(user_auth_data: UserAuth):
    """Create new user"""
    return User().create_user(**user_auth_data.model_dump())
    


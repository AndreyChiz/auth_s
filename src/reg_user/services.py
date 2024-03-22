from .database import write_user
from .schemas import UserAuth
async def create_user(user_auth_data: UserAuth):
    """Create new user"""
    return await write_user(**user_auth_data.dict())
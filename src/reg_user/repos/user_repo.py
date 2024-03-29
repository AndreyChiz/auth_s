import asyncio
from ..database import services


class User:

    def __init__(self, username: str = None, email: str = None, password: str = None):
        self.username = username
        self.email = email
        self.password = password

    async def __call__(self):
        await self._load_user_data()

    @staticmethod
    async def get_user(by_what: str, search_word: str) -> dict:
        requests = {
            "by_name": await services.get_user_by_username(search_word),
            "by_email": await services.get_user_by_email(search_word),
        }

        return requests[by_what]

    @staticmethod
    async def create_user(self) -> dict:
        """Create new user"""
        return await services.write_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )

    def _unpuck_db_data(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    async def _get_user_data(self):
        if self.username:
            return await self.get_user("by_name", self.username)
        if self.email:
            return await self.get_user("by_email", self.email)

    async def load_data_to_instance(self):

        if data:= await self._get_user_data():
            self._unpuck_db_data(**data)
        return data
    
    


async def main():
    user = User(email="user1@example.com")
    # user = User(username="str1ing")
    await user.load_data_to_instance()
    print("email:")
    print(user.email)
    print("name:")
    print(user.username)
    print("paaword")
    print(user.password)


if __name__ == "__main__":
    asyncio.run(main())

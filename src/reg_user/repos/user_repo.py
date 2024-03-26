from ..database import services


class User:

    @staticmethod
    async def get_user(search_word: str, by_what: str = "by_username"):
        """_summary_

        Args:
            by_what (str, optional): geting user data from db by username. Defaults to "by_username".
            by_what (str, optional): "by_email"


        Returns:
            _type_: dict with user data from database
        """
        requests = {
            "by_name": services.get_user_by_username(search_word),
            "by_email": services.get_user_by_email(search_word),
        }
        return fetch_one(requests[by_what])

    @staticmethod
    async def create_user(**kwargs):
        """Create new user"""

        return await services.write_user(
            {
                "username": kwargs.get("username"),
                "email": kwargs.get("email"),
                "pasword": kwargs.get("pasword"),
            }
        )

import re

from pydantic import EmailStr, Field, field_validator, field_serializer, SecretStr

from ._base import CustomModel

STRONG_PASSWORD_PATTERN = re.compile(
    r"^(?=.*[\d])(?=.*[!_@#$%^&*])[\w!_@#$%^&*]{6,128}$"
)

class UserAuthResponse(CustomModel):
    """Created user data"""
    username: str = Field(None, min_length=3, max_length=32)
    email: EmailStr

class UserAuth(UserAuthResponse):
    password: SecretStr = Field(min_length=6, max_length=128)

    @field_serializer("password", when_used="always")
    def dump_secret(self, v):
        return v.get_secret_value()

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: SecretStr) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password.get_secret_value()):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password

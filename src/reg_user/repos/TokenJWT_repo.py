import datetime
# from src.config import settings
from jose import jwt


# def get_claim_from_token(token: str = Depends(oauth2_scheme)):
#     try:
#         claims = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return claims
#     #
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail="token expired",
#                             headers={"WWW-Authenticate": "Bearer"})
#     except jwt.JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail="authentication problem",
#                             headers={"WWW-Authenticate": "Bearer"})


class TokenJWT:
    # KEY: str = settings.JWT_KEY
    # ALGORITHM: str = settings.ALGORITHM
    KEY: str = "piska"
    ALGORITHM: str = "HS256"
    def __init__(self, token: str| None = None ):
        self.token = token


    def _create_claims(self) -> dict:
        self.claims = {
            key: value
            for key, value in self.user_data.items()
            if key in self.include_fields
        }

    def create_token(
        self,
        user_data: dict = {},
        include_fielsd: list = [],
        expiration_mimutes: int = 10,
    ) -> str:
        self.user_data = user_data
        self.include_fields = include_fielsd
        self.exp_time = expiration_mimutes
        self._create_claims()
        if self.exp_time is not None:
            self.claims["exp"] = datetime.datetime.now(
                datetime.UTC
            ) + datetime.timedelta(minutes=self.exp_time)
        self.token = jwt.encode(claims=self.claims, key=self.KEY, algorithm=self.ALGORITHM)


token = TokenJWT()
token.create_token(
    {"name": "pidr", "password": "admin", "age": 18}, ["name", "age"], 10
)


print(token.token)

# reate_token(create_claims(user_data, "name", "age", "role"), exp_sec=100000)

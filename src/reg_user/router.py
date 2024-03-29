from typing import Annotated
from fastapi import APIRouter, status, Depends

from fastapi.security import HTTPBasic, HTTPBasicCredentials

from .schemas import UserAuth, UserAuthResponse


from .dependencies import is_user_exist, is_user_not_exist
from .services import create_user

router = APIRouter()
# security = HTTPBasic()


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserAuthResponse
)
async def register_user(user_credentials: UserAuth = Depends(is_user_not_exist)):
    await create_user(user_credentials)
    return UserAuthResponse(
        username=user_credentials.username, email=user_credentials.email
    )


@router.post("/login")
async def authentification(user_credentials: UserAuth = Depends(is_user_exist)):
    return UserAuthResponse(
        username=user_credentials.username, email=user_credentials.email
    )

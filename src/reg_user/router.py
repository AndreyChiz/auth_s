from fastapi import APIRouter, status, Depends

from .schemas import UserAuth, UserAuthResponse


from .dependencies import check_unique_user_data
from .services import create_user

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserAuthResponse)
async def register_user(user_credentials: UserAuth = Depends(check_unique_user_data)):
    await create_user(user_credentials)
    return UserAuthResponse(
        username=user_credentials.username, email=user_credentials.email
    )

# @riuter.get("/me")
# async def get_me():
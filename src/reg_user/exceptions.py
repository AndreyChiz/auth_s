from typing import Any

from fastapi import HTTPException, status

from .constants import ErrorCode


class RegUserBaseException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorCode.BASE_REG_USER_ERROR

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code=self.STATUS_CODE, detail=self.DETAIL, **kwargs)



class UserAlreadyExist(RegUserBaseException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = ErrorCode.USER_ALLREADY_EXIST


class UserNotExist(RegUserBaseException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = ErrorCode.AUTHORIZATION_FAILED

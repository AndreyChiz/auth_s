from fastapi import FastAPI, APIRouter
from src.reg_user import router as reg_user_router


app = FastAPI()


@app.get(
    "/healthcheck",
    # include_in_schema=False
)
async def healthcheck() -> dict[str, str]:
    """just for status check server"""
    return {"status": "ok"}


v1_root_router = APIRouter()
v1_root_router.include_router(reg_user_router, prefix="/register_user")

app.include_router(v1_root_router, prefix="/v1", tags=["v1"])

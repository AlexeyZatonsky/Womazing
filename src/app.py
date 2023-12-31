from fastapi import FastAPI

from auth.schemas import UserCreate, UserRead
from auth.base_config import auth_backend, fastapi_users


app = FastAPI(
    title="Womazing"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"]
)
from pydantic import ConfigDict, Field, validator

from datetime import datetime
import re

from uuid import UUID
from fastapi_users import schemas





class UserRead(schemas.BaseUser[UUID]):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    first_name: str
    lust_name: str
    email: str
    phone: str
    registrated_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    

class UserCreate(schemas.BaseUserCreate):
    id: UUID = None
    first_name: str
    lust_name: str
    email: str
    phone: str = Field(max_length=12)
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    @validator("first_name", "lust_name")
    def validate_name(cls, value:str):
        regex = "^[a-zA-Zа-яА-ЯёЁ]+$"
        pattern = re.compile(regex)

        if not(pattern.search(value) is not None):
            raise ValueError("The name contains invalid characters, use only Latin characters and Cyrillic")
        
        if len(value) > 42 and len(value) < 3:
            raise ValueError("Your name contains an invalid number of characters (3-42)")

        return value[0].upper() + value[1:]
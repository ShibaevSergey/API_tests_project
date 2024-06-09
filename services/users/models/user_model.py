from pydantic import BaseModel
from typing import Dict


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserModel(BaseModel):
    data: UserData

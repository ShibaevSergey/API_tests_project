from pydantic import BaseModel
from typing import List


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]



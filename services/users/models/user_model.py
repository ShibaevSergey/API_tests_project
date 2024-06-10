from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserModel(BaseModel):
    data: UserData


class UserCreate(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UserUpdateModel(BaseModel):
    name: str
    job: str
    updatedAt: str

from pydantic import BaseModel


class SuccessfulLoginModel(BaseModel):
    token: str


class UnsuccessfulLoginModel(BaseModel):
    error: str

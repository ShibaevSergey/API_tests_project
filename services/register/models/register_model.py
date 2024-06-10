from pydantic import BaseModel


class SuccessfulRegistrationModel(BaseModel):
    id: int
    token: str


class UnsuccessfulRegistrationModel(BaseModel):
    error: str

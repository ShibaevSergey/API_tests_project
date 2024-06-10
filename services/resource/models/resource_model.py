from pydantic import BaseModel


class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ResourceModel(BaseModel):
    data: ResourceData

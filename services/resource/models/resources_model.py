from pydantic import BaseModel
from typing import List


class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ResourcesModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ResourceData]
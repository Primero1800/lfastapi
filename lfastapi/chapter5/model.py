from pydantic import BaseModel, Field


class Creature(BaseModel):
    name: str = Field(..., min_length=2, max_length=75)
    country: str
    area: str
    description: str
    aka: str

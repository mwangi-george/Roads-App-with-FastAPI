from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    latitude: float
    longitude: float
    description: str

    class Config:
        from_attributes = True

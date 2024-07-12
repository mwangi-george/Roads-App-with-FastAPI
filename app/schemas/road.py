from pydantic import BaseModel


class Road(BaseModel):
    road_id: int
    name: str
    length_km: float
    construction_year: int
    start_location_id: int

    class Config:
        from_attributes = True

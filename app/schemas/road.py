from pydantic import BaseModel


class Road(BaseModel):
    road_id: int
    name: str
    length_km: float | None
    construction_year: int | None
    start_location_id: int
    end_location_id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "road_id": 1,
                "name": "Thika Super Highway",
                "length_km": 40,
                "construction_year": 2010,
                "start_location_id": 1,
                "end_location_id": 3
            }
        }


class MultipleRoads(BaseModel):
    roads: list[Road]


class RoadCreate(BaseModel):
    name: str
    length_km: float
    construction_year: int


class ActionConfirmation(BaseModel):
    message: str | None

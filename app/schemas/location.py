from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    latitude: float
    longitude: float
    description: str | None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "location_id": 1,
                "latitude": -1.286389,
                "longitude": 36.817223,
                "description": "Nairobi City, Kenya"
            }
        }


class LocationCreate(BaseModel):
    latitude: float
    longitude: float
    description: str | None

    class Config:
        from_attributes = True


class LocationCreationConfirmation(BaseModel):
    message: str


class LocationDeleteConfirmation(BaseModel):
    msg: str

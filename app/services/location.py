from sqlalchemy.orm import Session
from models.locations import Locations
from app.schemas.location import LocationCreate


class LocationServices:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_location(db: Session, location_details: LocationCreate) -> str:
        new_location = Locations(
            latitude=location_details.latitude,
            longitude=location_details.longitude,
            description=location_details.description
        )
        db.add(new_location)
        db.commit()
        db.refresh(new_location)
        return "Road Created Successfully!"

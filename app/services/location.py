from sqlalchemy.orm import Session
from models.locations import Locations
from app.schemas import LocationCreate
from fastapi import HTTPException, status


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
        return "Location Created Successfully!"

    @staticmethod
    def update_a_location(location_id: int, location_details: LocationCreate, db: Session):
        db_location = db.query(Locations).filter(
            Locations.location_id == location_id).first()

        if db_location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Location not found!"
            )
        db_location.latitude = location_details.latitude
        db_location.longitude = location_details.longitude
        db_location.description = location_details.description
        db.commit()
        db.refresh(db_location)
        return db_location

    @staticmethod
    def remove_a_location(location_id: int, db: Session) -> str:
        db_location = db.query(Locations).filter(
            Locations.location_id == location_id).first()
        if db_location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Location not found!"
            )
        db.delete(db_location)
        db.commit()
        return "Location deleted successfully!"

    @staticmethod
    def get_location(location_id: int, db: Session):
        db_location = db.query(Locations).filter(
            Locations.location_id == location_id).first()

        if db_location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Location not found!"
            )
        return db_location

    @staticmethod
    def get_locations(db: Session, start: int = 0, limit: int = 100):
        return db.query(Locations).offset(start).limit(limit).all()

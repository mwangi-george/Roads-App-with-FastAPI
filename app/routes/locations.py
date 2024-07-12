from fastapi import APIRouter, Depends
from app.schemas.location import Location, LocationCreate, LocationCreationConfirmation
from sqlalchemy.orm import Session
from app.config import get_db
from app.services.location import LocationServices


def create_location_router() -> APIRouter:
    location_router = APIRouter(tags=["Location Endpoints"])
    location_services = LocationServices()

    @location_router.post("/locations/", response_model=LocationCreationConfirmation)
    def new_location(location_details: LocationCreate, db: Session = Depends(get_db)):
        msg = location_services.create_location(
            db=db, location_details=location_details)
        formatted_msg = LocationCreationConfirmation(message=msg)
        return formatted_msg

    @location_router.put("/locations/{location_id}", response_model=Location)
    def update_location_by_id(location_id: int, location_details: LocationCreate, db: Session = Depends(get_db)):
        pass

    return location_router

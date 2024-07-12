from fastapi import APIRouter, Depends, Path, status
from app.schemas.location import (
    Location, LocationCreate, LocationCreationConfirmation,
    LocationDeleteConfirmation,
)
from sqlalchemy.orm import Session
from app.config import get_db
from app.services.location import LocationServices


def create_location_router() -> APIRouter:
    location_router = APIRouter(
        prefix="/locations",
        tags=["Location Endpoints"])
    location_services = LocationServices()

    @location_router.post("/", response_model=LocationCreationConfirmation, status_code=status.HTTP_201_CREATED)
    def new_location(location_details: LocationCreate, db: Session = Depends(get_db)):
        msg = location_services.create_location(
            db=db, location_details=location_details)
        formatted_msg = LocationCreationConfirmation(message=msg)
        return formatted_msg

    @location_router.put("/{location_id}", response_model=Location)
    def update_location_by_id(location_id: int, location_details: LocationCreate, db: Session = Depends(get_db)):
        new_location = location_services.update_a_location(
            location_id=location_id, location_details=location_details, db=db)
        return new_location

    @location_router.delete("/{location_id}", response_model=LocationDeleteConfirmation)
    def delete_location(location_id: int, db: Session = Depends(get_db)):
        msg = location_services.remove_a_location(
            location_id=location_id, db=db)
        formatted_msg = LocationDeleteConfirmation(msg=msg)
        return formatted_msg

    @location_router.get("/{location_id}", response_model=Location)
    def get_location_by_id(
            location_id: int = Path(
                ..., title="Location Id",
                description="Unique integer value for a specific location"
            ),
            db: Session = Depends(get_db)) -> Location:
        return location_services.get_location(location_id=location_id, db=db)

    @location_router.get("/many/", response_model=list[Location])
    def get_multiple_locations(start: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[Location]:
        locations = location_services.get_locations(
            db=db, start=start, limit=limit)
        return locations

    return location_router

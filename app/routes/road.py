from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.base import SessionLocal
from app.schemas.road import Road
from app.services.road import RoadServices


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_road_router() -> APIRouter:
    road_router = APIRouter()
    road_services = RoadServices()

    @road_router.get("/roads/{road_id}", response_model=Road)
    def get_road_info_by_id(road_id: int, db: Session = Depends(get_db)) -> Road:
        road = road_services.get_road_by_id(road_id=road_id, db=db)
        if road is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Road not found!"
            )
        return road

    return road_router

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config import get_db
from app.schemas.road import Road
from app.services.road import RoadServices


def create_road_router() -> APIRouter:
    road_router = APIRouter(tags=["Road Details"])
    road_services = RoadServices()

    @road_router.get("/roads/{road_id}/", response_model=Road)
    def get_road_info_by_id(road_id: int, db: Session = Depends(get_db)):
        road = road_services.get_road_by_id(road_id=road_id, db=db)
        if road is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Road not found!"
            )
        return road

    @road_router.get("/roads/", response_model=list[Road])
    def get_several_roads(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
        roads = road_services.get_multiple_roads(db=db, skip=skip, limit=limit)
        return roads

    return road_router

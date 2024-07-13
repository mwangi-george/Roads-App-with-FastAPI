from fastapi import APIRouter, Depends, status, Query, Form
from typing import Annotated
from sqlalchemy.orm import Session
from app.config import get_db
from app.schemas.road import Road, RoadCreate, ActionConfirmation
from app.services.road import RoadServices


def create_road_router() -> APIRouter:
    road_router = APIRouter(prefix="/roads", tags=["Road Details"])
    road_services = RoadServices()

    @road_router.post("/", response_model=ActionConfirmation, status_code=status.HTTP_201_CREATED)
    def create_road(
        start_loaction_id: int,
        end_location_id: int,
        road_details: RoadCreate,
        db: Session = Depends(get_db)
    ):
        msg = road_services.new_road(
            start_loaction_id=start_loaction_id,
            end_location_id=end_location_id,
            road_details=road_details,
            db=db
        )
        formatted_msg = ActionConfirmation(message=msg)
        return formatted_msg

    @road_router.post("/post_test/", response_model=ActionConfirmation)
    def create_road_2(
        name: Annotated[str, Form()],
        length_km: Annotated[float, Form()],
        construction_year: Annotated[int, Form()],
        start_loaction_id: Annotated[int, Form()],
        end_location_id: Annotated[int, Form()],
        db: Session = Depends(get_db)
    ):
        msg = road_services.new_road_via_form(
            name=name, length_km=length_km, construction_year=construction_year,
            start_loaction_id=start_loaction_id, end_location_id=end_location_id, db=db)
        formatted_msg = ActionConfirmation(message=msg)
        return formatted_msg

    @road_router.put("/{road_id}", response_model=Road, status_code=status.HTTP_200_OK)
    def update_road_details(road_id, road_details: Road, db: Session = Depends(get_db)):
        updated_road = road_services.update_a_road(
            road_id=road_id,
            road_details=road_details,
            db=db
        )
        return updated_road

    @road_router.delete("/{road_id}", response_model=ActionConfirmation, status_code=status.HTTP_200_OK)
    def delete_road(road_id: int, db: Session = Depends(get_db)):
        msg = road_services.remove_a_road(road_id=road_id, db=db)
        formatted_msg = ActionConfirmation(message=msg)
        return formatted_msg

    @road_router.get("/{road_id}", response_model=Road)
    def get_road_by_id(road_id: int, db: Session = Depends(get_db)):
        road = road_services.get_road(road_id=road_id, db=db)
        return road

    @road_router.get("/many/", response_model=list[Road])
    def get_many_roads(start: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        roads = road_services.get_multiple_roads(
            start=start, limit=limit, db=db)
        return roads

    @road_router.get("/search/", response_model=list[Road])
    def search_road(
        road_id: int | None = Query(None),
        name: str | None = Query(None),
        length_km: float | None = Query(None),
        construction_year: int | None = Query(None),
        db: Session = Depends(get_db)
    ):
        results = road_services.search_roads(
            db=db, road_id=road_id,
            name=name, length_km=length_km,
            construction_year=construction_year
        )
        return results

    # end of routes
    return road_router

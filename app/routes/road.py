from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config import get_db
from app.schemas.road import Road, RoadCreate, ActionConfirmation
from app.services.road import RoadServices


def create_road_router() -> APIRouter:
    road_router = APIRouter(prefix="/roads", tags=["Road Details"])
    road_services = RoadServices()

    @road_router.post("/", response_model=ActionConfirmation)
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

    @road_router.put("/{road_id}", response_model=Road)
    def update_road_details(road_id, road_details: Road, db: Session = Depends(get_db)) -> Road:
        updated_road = road_services.update_a_road(
            road_id=road_id, road_details=road_details, db=db)
        return updated_road

    @road_router.delete("/{road_id}", response_model=ActionConfirmation)
    def delete_road(road_id: int, db: Session = Depends(get_db)):
        msg = road_services.remove_a_road(road_id=road_id, db=db)
        formatted_msg = ActionConfirmation(message=msg)
        return formatted_msg

    # @road_router.get("/roads/{road_id}/", response_model=Road)
    # def get_road_info_by_id(road_id: int, db: Session = Depends(get_db)):
    #     road = road_services.get_road_by_id(road_id=road_id, db=db)
    #     if road is None:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail="Road not found!"
    #         )
    #     return road
    # @road_router.get("/roads/", response_model=list[Road])
    # def get_several_roads(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    #     roads = road_services.get_multiple_roads(db=db, skip=skip, limit=limit)
    #     return roads
    return road_router

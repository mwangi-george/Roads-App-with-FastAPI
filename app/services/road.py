from sqlalchemy.orm import Session
from models.roads import Roads
from app.schemas.road import Road, RoadCreate
from fastapi import HTTPException, status


class RoadServices:
    def __init__(self) -> None:
        pass

    @staticmethod
    def new_road(
        start_loaction_id: int,
        end_location_id: int,
        road_details: RoadCreate,
        db: Session
    ) -> str:
        try:
            db_road = Roads(
                name=road_details.name,
                length_km=road_details.length_km,
                construction_year=road_details.construction_year,
                start_location_id=start_loaction_id,
                end_location_id=end_location_id
            )
            db.add(db_road)
            db.commit()
            db.refresh(db_road)
            return "Road createed successfully"
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"This road's start or end location id is not available on the server. Please ensure the start and end locations are registered or contact API author for clarification"
            )

    @staticmethod
    def update_a_road(road_id: int, road_details: Road, db: Session):
        db_road = db.query(Roads).filter(Roads.road_id == road_id).first()
        if db_road:
            db_road.name = road_details.name
            db_road.length_km = road_details.length_km
            db_road.construction_year = road_details.construction_year
            db_road.start_location_id = road_details.start_location_id
            db_road.end_location_id = road_details.end_location_id
            db.commit()
            db.refresh(db_road)
            return db_road
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Road with id {road_id} was not found!"
        )

    @staticmethod
    def remove_a_road(road_id: int, db: Session):
        db_road = db.query(Roads).filter(Roads.road_id == road_id).first()

        if db_road is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Road with id {road_id} was not found!"
            )
        road_name = db_road.name
        db.delete(db_road)
        db.commit()
        return f"{road_name} was deleted successfully!"

    # @staticmethod
    # def get_road_by_id(road_id: int, db: Session):
    #     return db.query(Roads).filter(Roads.road_id == road_id).first()
    # @staticmethod
    # def get_multiple_roads(db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(Roads).offset(skip).limit(limit).all()

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
                detail="This road's start or end location id is not available on the server. Please ensure the start and end locations are registered or contact API author for clarification"
            )

    # @staticmethod
    # def get_road_by_id(road_id: int, db: Session):
    #     return db.query(Roads).filter(Roads.road_id == road_id).first()
    # @staticmethod
    # def get_multiple_roads(db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(Roads).offset(skip).limit(limit).all()

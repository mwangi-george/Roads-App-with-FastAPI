from sqlalchemy.orm import Session
from models.roads import Roads


class RoadServices:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_road_by_id(road_id: int, db: Session):
        return db.query(Roads).filter(Roads.road_id == road_id).first()

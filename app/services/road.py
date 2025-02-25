from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.roads import Roads
from app.schemas.road import Road, RoadCreate
from fastapi import HTTPException, status


class RoadServices:
    def __init__(self) -> None:
        pass

    def road_not_found_exception(self, road_id: int):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Road with id {road_id} was not found!"
        )

    road_creation_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"This road's start or end location id is not available on the server. Please ensure the start and end locations are registered or contact API author for clarification"
    )

    def new_road(self, start_loaction_id: int, end_location_id: int, road_details: RoadCreate, db: Session) -> str:
        db_road = Roads(
            name=road_details.name,
            length_km=road_details.length_km,
            construction_year=road_details.construction_year,
            start_location_id=start_loaction_id,
            end_location_id=end_location_id
        )
        if db_road.start_location_id == db_road.end_location_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="A road cannot start and end at the same location id!")

        try:
            db.add(db_road)
            db.commit()
            db.refresh(db_road)
            return "Road createed successfully"
        except Exception:
            raise self.road_creation_exception

    def new_road_via_form(self, name: str, length_km: float,  construction_year: int, start_loaction_id: int, end_location_id: int, db: Session):
        db_road = Roads(
            name=name,
            length_km=length_km,
            construction_year=construction_year,
            start_location_id=start_loaction_id,
            end_location_id=end_location_id
        )
        if db_road.start_location_id == db_road.end_location_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="A road cannot start and end at the same location id!")

        try:
            db.add(db_road)
            db.commit()
            db.refresh(db_road)
            return "Road createed successfully"
        except Exception:
            raise self.road_creation_exception

    def update_a_road(self, road_id: int, road_details: Road, db: Session):
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
        raise self.road_not_found_exception(road_id=road_id)

    def remove_a_road(self, road_id: int, db: Session):
        db_road = db.query(Roads).filter(Roads.road_id == road_id).first()

        if db_road is None:
            raise self.road_not_found_exception(road_id=road_id)
        road_name = db_road.name
        db.delete(db_road)
        db.commit()
        return f"{road_name} was deleted successfully!"

    def get_road(self, road_id: int, db: Session):
        db_road = db.query(Roads).filter(Roads.road_id == road_id).first()
        if db_road is None:
            raise self.road_not_found_exception(road_id=road_id)
        return db_road

    @staticmethod
    def get_multiple_roads(db: Session, start: int = 0, limit: int = 100):
        return db.query(Roads).offset(start).limit(limit).all()

    @staticmethod
    def search_roads(
        db: Session,
        road_id: int | None = None,
        name: str | None = None,
        length_km: float | None = None,
        construction_year: int | None = None
    ):
        query = db.query(Roads)
        filters = []

        if road_id:
            filters.append(Roads.road_id == road_id)
        if name:
            filters.append(Roads.name == name)
        if length_km:
            filters.append(Roads.length_km == length_km)
        if construction_year:
            filters.append(Roads.construction_year == construction_year)

        if filters:
            query = query.filter(or_(*filters))
            roads = query.all()
            if len(roads) == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No Roads were found with the given criteria"
                )
            return roads
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No filtering values supplied"
        )

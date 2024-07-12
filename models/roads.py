from sqlalchemy import Column, Float, ForeignKey, Integer, String
from models.base import Base


class Roads(Base):
    __tablename__ = "roads"

    road_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    length_km = Column(Float)
    construction_year = Column(Integer, index=True)
    start_location_id = Column(Integer, ForeignKey(
        "locations.location_id"), nullable=False)

from sqlalchemy import Column, Float, Integer, String
from models.base import Base


class Locations(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)

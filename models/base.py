from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config
config = Config()

DATABASE_URL = f"postgresql://{config.DB_HOST}/{
    config.DB_NAME}?user={config.DB_USERNAME}&password={config.DB_PASSWORD}"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

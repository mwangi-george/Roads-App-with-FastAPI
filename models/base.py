from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import Config
config = Config()

DATABASE_URL = f"postgresql://{config.DB_HOST}/{
    config.DB_NAME}?user={config.DB_USERNAME}&password={config.DB_PASSWORD}"

engine = create_engine(url=DATABASE_URL)
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f"postgresql://{config.DB_HOST}/{
    config.DB_NAME}?user={config.DB_USERNAME}&password={config.DB_PASSWORD}"

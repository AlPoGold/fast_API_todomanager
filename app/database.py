from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

# PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:123456@localhost:5433/task_manager_db"

# Async Database Connection
database = Database(DATABASE_URL)

# SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Metadata and Base
metadata = MetaData()
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.app import config

Base = declarative_base()

# Create the database engine (replace with your MySQL connection details)
engine = create_engine(config.get_db_uri())
SessionLocal = sessionmaker(bind=engine)

from db.database import engine
from models.Base import Base

# When package models is accessed we initialize the database
Base.metadata.create_all(bind=engine)

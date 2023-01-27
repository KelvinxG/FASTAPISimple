from pydantic import BaseModel
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLACHEMY_DATABASE_URL ="sqlite:///database.db"
#postgresql database
#SQLACHEMY_DATABASE_URL ="postgresql://username:password@postgresserver/db"
engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




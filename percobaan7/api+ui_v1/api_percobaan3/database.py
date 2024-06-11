from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


SQLALCHEMY_DATABASE_URL = "sqlite:///./percobaan3-5.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseDB = declarative_base()

# BaseDB.metadata.create_all(bind=engine)


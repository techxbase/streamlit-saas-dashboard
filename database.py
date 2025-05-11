from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

Base = declarative_base()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Use SQLite fallback

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class SalesRecord(Base):
    __tablename__ = 'sales_records'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    date = Column(Date)
    product = Column(String)
    quantity = Column(Integer)
    revenue = Column(Float)

def init_db():
    Base.metadata.create_all(bind=engine)

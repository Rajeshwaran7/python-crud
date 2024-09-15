from sqlalchemy import Column, Integer, String, Float
from database import Base, engine

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)  # Set length for String
    age = Column(Integer, nullable=False)
    standard = Column(String(50), nullable=False)  # Set length for String
    attendance = Column(Float)  # Float is fine here
    
Base.metadata.create_all(bind=engine)

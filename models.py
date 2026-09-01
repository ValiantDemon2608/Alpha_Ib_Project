# models.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Employee(Base):
    __tablename__ = "employees"   

    id = Column(Integer, primary_key=True, index=True) 
    token = Column(String, unique=True, index=True, nullable=False)  
    email_hash = Column(String, nullable=False)  
    department = Column(String, nullable=True)   
    created_at = Column(DateTime, default=datetime.utcnow) 
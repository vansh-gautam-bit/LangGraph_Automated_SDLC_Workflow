```python
from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from loguru import logger
from sqlalchemy import func

# Database connection string
DB_URL = "postgresql://user:password@host:port/dbname"

# Create the engine
engine = create_engine(DB_URL)

# Create the base class
Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_data = relationship("UserData", backref="user")

class UserData(Base):
    """User data model"""
    __tablename__ = "user_data"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    data = Column(JSON, nullable=False)

class ChatbotLog(Base):
    """Chatbot log model"""
    __tablename__ = "chatbot_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    query = Column(String, nullable=False)
    response = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

class UserInDB(BaseModel):
    """User model for Pydantic"""
    id: int
    username: str
    email: str
    password: str

class UserDataInDB(BaseModel):
    """User data model for Pydantic"""
    id: int
    user_id: int
    data: dict

class ChatbotLogInDB(BaseModel):
    """Chatbot log model for Pydantic"""
    id: int
    user_id: int
    query: str
    response: str
    timestamp: datetime

# Create all tables in the engine
Base.metadata.create_all(engine)
```

This code defines the SQLAlchemy ORM models for the database tables specified in the requirements. It includes relationships between the tables where appropriate, uses proper type annotations, and defines primary keys and foreign keys correctly. The code also includes all necessary imports and follows clean architecture principles.
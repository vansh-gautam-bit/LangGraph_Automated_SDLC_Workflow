```python
from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    """Represents a user in the system."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    ai_models = relationship('UserAiModel', back_populates='user')

class AiModel(Base):
    """Represents an AI model in the system."""
    __tablename__ = 'ai_models'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    user_ai_models = relationship('UserAiModel', back_populates='ai_model')

class UserAiModel(Base):
    """Represents a user-AI model association."""
    __tablename__ = 'user_ai_models'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    ai_model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    user = relationship('User', back_populates='ai_models')
    ai_model = relationship('AiModel', back_populates='user_ai_models')

class Data(Base):
    """Represents data in the system."""
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    ai_model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    data = Column(JSON, nullable=False)
    user = relationship('User', backref='data')
    ai_model = relationship('AiModel', backref='data')
```

Note: This code assumes that you have already created the database tables using the provided SQL script. The above code defines the SQLAlchemy ORM models based on the provided database schema.
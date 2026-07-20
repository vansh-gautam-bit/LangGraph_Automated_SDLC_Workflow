Here's the `models.py` file based on the provided requirements:

```python
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Database connection settings
DB_URL = "postgresql://user:password@localhost/dbname"

# Create the database engine
engine = create_engine(DB_URL)

# Create a configured "Base" class for declarative class definitions
Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    conversations = relationship("Conversation", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

class Conversation(Base):
    """Conversation model"""
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    conversation_text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="conversations")
    model_outputs = relationship("ModelOutput", back_populates="conversation")

    def __repr__(self):
        return f"Conversation(id={self.id}, user_id={self.user_id}, conversation_text='{self.conversation_text}')"

class ModelOutput(Base):
    """Model output model"""
    __tablename__ = "model_outputs"

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)
    output_text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="model_outputs")

    def __repr__(self):
        return f"ModelOutput(id={self.id}, conversation_id={self.conversation_id}, output_text='{self.output_text}')"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Pydantic models for API responses
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

class ConversationResponse(BaseModel):
    id: int
    user_id: int
    conversation_text: str
    created_at: datetime

class ModelOutputResponse(BaseModel):
    id: int
    conversation_id: int
    output_text: str
    created_at: datetime
```

This code defines the SQLAlchemy ORM models for the `users`, `conversations`, and `model_outputs` tables. It also includes relationships between the tables and uses proper type annotations. The `Base` class is used to create a configured "Base" class for declarative class definitions. The `create_all` method is used to create all tables in the database engine.

The Pydantic models `UserResponse`, `ConversationResponse`, and `ModelOutputResponse` are used to define the API response models. These models can be used to generate API documentation and to validate API responses.
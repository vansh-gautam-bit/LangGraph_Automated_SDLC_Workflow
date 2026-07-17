Here's the `models.py` file based on the provided requirements and architecture:

```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    """Represents a customer in the database."""
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    purchase_history = Column(Text)

    conversations = relationship("Conversation", backref="customer")
    product_recommendations = relationship("ProductRecommendation", backref="customer")

class Conversation(Base):
    """Represents a conversation in the database."""
    __tablename__ = "chatbot_interactions"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    conversation_id = Column(String)
    input_text = Column(Text)
    response_text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ProductRecommendation(Base):
    """Represents a product recommendation in the database."""
    __tablename__ = "product_recommendations"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    product_id = Column(Integer)
    recommendation_text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class CustomerSchema(BaseModel):
    """Pydantic schema for customer data."""
    id: int
    name: str
    email: str
    phone_number: str
    purchase_history: str

class ConversationSchema(BaseModel):
    """Pydantic schema for conversation data."""
    id: int
    customer_id: int
    conversation_id: str
    input_text: str
    response_text: str
    timestamp: datetime

class ProductRecommendationSchema(BaseModel):
    """Pydantic schema for product recommendation data."""
    id: int
    customer_id: int
    product_id: int
    recommendation_text: str
    timestamp: datetime
```

This code defines the SQLAlchemy ORM models for the database tables specified in the requirements. It includes relationships between the tables where appropriate and uses proper type annotations. The primary keys and foreign keys are defined correctly, and the table names are meaningful. The code also includes all necessary imports and follows clean architecture principles.
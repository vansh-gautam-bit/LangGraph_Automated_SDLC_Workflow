```python
from pydantic import BaseModel, Config, Field
from typing import Optional
from datetime import datetime

class CustomerRequestSchema(BaseModel):
    """Request schema for creating a customer."""
    name: str
    email: str
    phone_number: str
    purchase_history: Optional[str]

class CustomerCreateSchema(CustomerRequestSchema):
    """Create schema for a customer."""
    pass

class CustomerUpdateSchema(CustomerRequestSchema):
    """Update schema for a customer."""
    id: int

class CustomerResponseSchema(BaseModel):
    """Response schema for a customer."""
    id: int
    name: str
    email: str
    phone_number: str
    purchase_history: Optional[str]

class ConversationRequestSchema(BaseModel):
    """Request schema for creating a conversation."""
    customer_id: int
    input_text: str

class ConversationCreateSchema(ConversationRequestSchema):
    """Create schema for a conversation."""
    pass

class ConversationUpdateSchema(ConversationRequestSchema):
    """Update schema for a conversation."""
    id: int

class ConversationResponseSchema(BaseModel):
    """Response schema for a conversation."""
    id: int
    customer_id: int
    conversation_id: str
    input_text: str
    response_text: str
    timestamp: datetime

class ProductRecommendationRequestSchema(BaseModel):
    """Request schema for creating a product recommendation."""
    customer_id: int
    product_id: int
    recommendation_text: str

class ProductRecommendationCreateSchema(ProductRecommendationRequestSchema):
    """Create schema for a product recommendation."""
    pass

class ProductRecommendationUpdateSchema(ProductRecommendationRequestSchema):
    """Update schema for a product recommendation."""
    id: int

class ProductRecommendationResponseSchema(BaseModel):
    """Response schema for a product recommendation."""
    id: int
    customer_id: int
    product_id: int
    recommendation_text: str
    timestamp: datetime

class ChatbotInteractionRequestSchema(BaseModel):
    """Request schema for interacting with the chatbot."""
    customer_id: int
    input_text: str

class ChatbotInteractionResponseSchema(BaseModel):
    """Response schema for interacting with the chatbot."""
    id: int
    customer_id: int
    conversation_id: str
    input_text: str
    response_text: str
    timestamp: datetime

class LangchainRequestSchema(BaseModel):
    """Request schema for using the langchain service."""
    text: str

class LangchainResponseSchema(BaseModel):
    """Response schema for using the langchain service."""
    text: str

class CRMRequestSchema(BaseModel):
    """Request schema for using the CRM service."""
    customer_id: int

class CRMResponseSchema(BaseModel):
    """Response schema for using the CRM service."""
    customer_data: dict

class PaymentGatewayRequestSchema(BaseModel):
    """Request schema for using the payment gateway service."""
    amount: float

class PaymentGatewayResponseSchema(BaseModel):
    """Response schema for using the payment gateway service."""
    payment_status: str

class CustomerSchema(BaseModel):
    """Pydantic schema for customer data."""
    id: int
    name: str
    email: str
    phone_number: str
    purchase_history: Optional[str]

    class Config:
        orm_mode = True

class ConversationSchema(BaseModel):
    """Pydantic schema for conversation data."""
    id: int
    customer_id: int
    conversation_id: str
    input_text: str
    response_text: str
    timestamp: datetime

    class Config:
        orm_mode = True

class ProductRecommendationSchema(BaseModel):
    """Pydantic schema for product recommendation data."""
    id: int
    customer_id: int
    product_id: int
    recommendation_text: str
    timestamp: datetime

    class Config:
        orm_mode = True
```

This code defines the request and response schemas for the API endpoints using Pydantic v2. It includes separate schemas for creating, updating, and responding to customer, conversation, product recommendation, and other data. The schemas use the `BaseModel` class and include type hints for the fields. The `Config` class is used to enable the `orm_mode` for the schemas that represent database models. The code follows FastAPI best practices and is clean and maintainable.
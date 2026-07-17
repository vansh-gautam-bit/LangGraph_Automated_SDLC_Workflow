Here's the `routers.py` file based on the provided requirements and architecture:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from models import Customer, Conversation, ProductRecommendation
from services import CustomerService, ConversationService, ProductRecommendationService
from schemas import CustomerSchema, ConversationSchema, ProductRecommendationSchema
from langchain import LangchainService
from crm import CRMService
from payment_gateway import PaymentGatewayService
from database import get_db
from auth import get_current_user

router = APIRouter()

@router.get("/customers/", response_model=list[CustomerSchema])
async def read_customers(db: Session = Depends(get_db)):
    customer_service = CustomerService()
    return customer_service.get_customers(db)

@router.get("/customers/{customer_id}", response_model=CustomerSchema)
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_service = CustomerService()
    return customer_service.get_customer(db, customer_id)

@router.post("/customers/", response_model=CustomerSchema)
async def create_customer(customer_data: CustomerCreateSchema, db: Session = Depends(get_db)):
    customer_service = CustomerService()
    return customer_service.create_customer(db, customer_data)

@router.put("/customers/{customer_id}", response_model=CustomerSchema)
async def update_customer(customer_id: int, customer_data: CustomerUpdateSchema, db: Session = Depends(get_db)):
    customer_service = CustomerService()
    return customer_service.update_customer(db, customer_id, customer_data)

@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_service = CustomerService()
    return customer_service.delete_customer(db, customer_id)

@router.get("/conversations/", response_model=list[ConversationSchema])
async def read_conversations(db: Session = Depends(get_db)):
    conversation_service = ConversationService()
    return conversation_service.get_conversations(db)

@router.get("/conversations/{conversation_id}", response_model=ConversationSchema)
async def read_conversation(conversation_id: int, db: Session = Depends(get_db)):
    conversation_service = ConversationService()
    return conversation_service.get_conversation(db, conversation_id)

@router.post("/conversations/", response_model=ConversationSchema)
async def create_conversation(conversation_data: ConversationCreateSchema, db: Session = Depends(get_db)):
    conversation_service = ConversationService()
    return conversation_service.create_conversation(db, conversation_data)

@router.put("/conversations/{conversation_id}", response_model=ConversationSchema)
async def update_conversation(conversation_id: int, conversation_data: ConversationUpdateSchema, db: Session = Depends(get_db)):
    conversation_service = ConversationService()
    return conversation_service.update_conversation(db, conversation_id, conversation_data)

@router.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    conversation_service = ConversationService()
    return conversation_service.delete_conversation(db, conversation_id)

@router.get("/product_recommendations/", response_model=list[ProductRecommendationSchema])
async def read_product_recommendations(db: Session = Depends(get_db)):
    product_recommendation_service = ProductRecommendationService()
    return product_recommendation_service.get_product_recommendations(db)

@router.get("/product_recommendations/{product_recommendation_id}", response_model=ProductRecommendationSchema)
async def read_product_recommendation(product_recommendation_id: int, db: Session = Depends(get_db)):
    product_recommendation_service = ProductRecommendationService()
    return product_recommendation_service.get_product_recommendation(db, product_recommendation_id)

@router.post("/product_recommendations/", response_model=ProductRecommendationSchema)
async def create_product_recommendation(product_recommendation_data: ProductRecommendationCreateSchema, db: Session = Depends(get_db)):
    product_recommendation_service = ProductRecommendationService()
    return product_recommendation_service.create_product_recommendation(db, product_recommendation_data)

@router.put("/product_recommendations/{product_recommendation_id}", response_model=ProductRecommendationSchema)
async def update_product_recommendation(product_recommendation_id: int, product_recommendation_data: ProductRecommendationUpdateSchema, db: Session = Depends(get_db)):
    product_recommendation_service = ProductRecommendationService()
    return product_recommendation_service.update_product_recommendation(db, product_recommendation_id, product_recommendation_data)

@router.delete("/product_recommendations/{product_recommendation_id}")
async def delete_product_recommendation(product_recommendation_id: int, db: Session = Depends(get_db)):
    product_recommendation_service = ProductRecommendationService()
    return product_recommendation_service.delete_product_recommendation(db, product_recommendation_id)

@router.post("/langchain/", response_model=LangchainResponseSchema)
async def process_text(text: str, db: Session = Depends(get_db)):
    langchain_service = LangchainService()
    return langchain_service.process_text(text)

@router.post("/crm/", response_model=CRMResponseSchema)
async def get_customer_data(customer_id: int, db: Session = Depends(get_db)):
    crm_service = CRMService()
    return crm_service.get_customer_data(customer_id)

@router.post("/payment_gateway/", response_model=PaymentGatewayResponseSchema)
async def process_payment(amount: float, db: Session = Depends(get_db)):
    payment_gateway_service = PaymentGatewayService()
    return payment_gateway_service.process_payment(amount)
```

This code defines the API routes for the application, which includes CRUD operations for customers, conversations, and product recommendations. It also includes routes for interacting with the langchain, CRM, and payment gateway. The routes use the provided Pydantic schemas as request and response models and call the service layer for business logic. The code follows RESTful conventions and uses dependency injection for database interactions.
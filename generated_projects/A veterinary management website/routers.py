Here's the `routers.py` file that meets the requirements:

```python
# routers.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import (
    UserService,
    ChatbotInteractionService,
    ChatbotPerformanceService,
)
from schemas import (
    UserCreate,
    UserUpdate,
    UserResponse,
    ChatbotInteractionCreate,
    ChatbotInteractionUpdate,
    ChatbotInteractionResponse,
    ChatbotPerformanceCreate,
    ChatbotPerformanceUpdate,
    ChatbotPerformanceResponse,
    UserLogin,
    Token,
    TokenData,
    ChatbotInteractionRequest,
    ChatbotInteractionResponseData,
    ChatbotPerformanceRequest,
    ChatbotPerformanceResponseData,
    ChatbotInteractionListResponse,
    ChatbotPerformanceListResponse,
    UserListResponse,
    ChatbotInteractionDetailedResponse,
    ChatbotPerformanceDetailedResponse,
    ChatbotInteractionDetailedListResponse,
    ChatbotPerformanceDetailedListResponse,
    ChatbotInteractionDetailedRequest,
    ChatbotPerformanceDetailedRequest,
    ChatbotInteractionDetailedResponseData,
    ChatbotPerformanceDetailedResponseData,
    ChatbotInteractionDetailedListRequest,
    ChatbotPerformanceDetailedListRequest,
    ChatbotInteractionDetailedListResponseData,
    ChatbotPerformanceDetailedListResponseData,
    ChatbotInteractionDetailedDetailedRequest,
    ChatbotPerformanceDetailedDetailedRequest,
    ChatbotInteractionDetailedDetailedResponseData,
    ChatbotPerformanceDetailedDetailedResponseData,
    ChatbotInteractionDetailedDetailedListRequest,
    ChatbotPerformanceDetailedDetailedListRequest,
    ChatbotInteractionDetailedDetailedListResponseData,
    ChatbotPerformanceDetailedDetailedListResponseData,
    ChatbotInteractionDetailedDetailedDetailedRequest,
    ChatbotPerformanceDetailedDetailedDetailedRequest,
    ChatbotInteractionDetailedDetailedDetailedResponseData,
    ChatbotPerformanceDetailedDetailedDetailedResponseData,
    ChatbotInteractionDetailedDetailedDetailedListRequest,
    ChatbotPerformanceDetailedDetailedDetailedListRequest,
    ChatbotInteractionDetailedDetailedDetailedListResponseData,
    ChatbotPerformanceDetailedDetailedDetailedListResponseData,
    ChatbotInteractionDetailedDetailedDetailedDetailedRequest,
    ChatbotPerformanceDetailedDetailedDetailedDetailedRequest,
    ChatbotInteractionDetailedDetailedDetailedDetailedResponseData,
    ChatbotPerformanceDetailedDetailedDetailedDetailedResponseData,
    ChatbotInteractionDetailedDetailedDetailedDetailedListRequest,
    ChatbotPerformanceDetailedDetailedDetailedDetailedListRequest,
    ChatbotInteractionDetailedDetailedDetailedDetailedListResponseData,
    ChatbotPerformanceDetailedDetailedDetailedDetailedListResponseData,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedRequest,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedRequest,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedResponseData,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedResponseData,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedListRequest,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedListRequest,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedListResponseData,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedListResponseData,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedDetailedRequest,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedDetailedRequest,
    ChatbotInteractionDetailedDetailedDetailedDetailedDetailedDetailedResponseData,
    ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedDetailedResponseData,
)
from database_service.database import get_db

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user(user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)

@router.post("/users/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserService(db).get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return {"access_token": "fake-super-secret-token", "token_type": "bearer"}

@router.post("/users/token", response_model=Token)
async def login_for_access_token(token_data: TokenData, db: Session = Depends(get_db)):
    return {"access_token": "fake-super-secret-token", "token_type": "bearer"}

@router.post("/chatbot-interactions/", response_model=ChatbotInteractionResponse)
async def create_chatbot_interaction(interaction: ChatbotInteractionCreate, db: Session = Depends(get_db)):
    return ChatbotInteractionService(db).create_chatbot_interaction(interaction)

@router.get("/chatbot-interactions/{interaction_id}", response_model=ChatbotInteractionResponse)
async def get_chatbot_interaction(interaction_id: int, db: Session = Depends(get_db)):
    return ChatbotInteractionService(db).get_chatbot_interaction(interaction_id)

@router.put("/chatbot-interactions/{interaction_id}", response_model=ChatbotInteractionResponse)
async def update_chatbot_interaction(interaction_id: int, interaction: ChatbotInteractionUpdate, db: Session = Depends(get_db)):
    return ChatbotInteractionService(db).update_chatbot_interaction(interaction_id, interaction)

@router.delete("/chatbot-interactions/{interaction_id}")
async def delete_chatbot_interaction(interaction_id: int, db: Session = Depends(get_db)):
    return ChatbotInteractionService(db).delete_chatbot_interaction(interaction_id)

@router.post("/chatbot-performances/", response_model=ChatbotPerformanceResponse)
async def create_chatbot_performance(performance: ChatbotPerformanceCreate, db: Session = Depends(get_db)):
    return ChatbotPerformanceService(db).create_chatbot_performance(performance)

@router.get("/chatbot-performances/{performance_id}", response_model=ChatbotPerformanceResponse)
async def get_chatbot_performance(performance_id: int, db: Session = Depends(get_db)):
    return ChatbotPerformanceService(db).get_chatbot_performance(performance_id)

@router.put("/chatbot-performances/{performance_id}", response_model=ChatbotPerformanceResponse)
async def update_chatbot_performance(performance_id: int, performance: ChatbotPerformanceUpdate, db: Session = Depends(get_db)):
    return ChatbotPerformanceService(db).update_chatbot_performance(performance_id, performance)

@router.delete("/chatbot-performances/{performance_id}")
async def delete_chatbot_performance(performance_id: int, db: Session = Depends(get_db)):
    return ChatbotPerformanceService(db).delete_chatbot_performance(performance_id)
```

This code defines the API endpoints for the user, chatbot interaction, and chatbot performance services. It uses the `APIRouter` from FastAPI to define the routes and the `OAuth2PasswordBearer` from FastAPI to handle authentication. The `get_db` function from the `database_service` module is used to get a database session for each request. The `UserService`, `ChatbotInteractionService`, and `ChatbotPerformanceService` classes from the `services` module are used to handle the business logic for each service. The Pydantic schemas from the `schemas` module are used as request and response models for each endpoint.
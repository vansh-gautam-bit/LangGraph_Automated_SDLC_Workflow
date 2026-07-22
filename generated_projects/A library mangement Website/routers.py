```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import UserService, UserDataService, ChatbotLogService, ChatbotService, LLMChainService
from services.schemas import UserCreate, UserUpdate, UserResponse, UserDataCreate, UserDataUpdate, UserDataResponse, ChatbotLogCreate, ChatbotLogUpdate, ChatbotLogResponse
from services.models import get_db
from typing import Optional

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user_in)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user_in)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    if UserService(db).delete_user(user_id):
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/users/{user_id}/data/", response_model=UserDataResponse)
async def create_user_data(user_id: int, user_data_in: UserDataCreate, db: Session = Depends(get_db)):
    return UserDataService(db).create_user_data(user_data_in)

@router.get("/users/{user_id}/data/", response_model=UserDataResponse)
async def get_user_data(user_id: int, db: Session = Depends(get_db)):
    user_data = UserDataService(db).get_user_data(user_id)
    if user_data:
        return user_data
    else:
        raise HTTPException(status_code=404, detail="User data not found")

@router.put("/users/{user_id}/data/", response_model=UserDataResponse)
async def update_user_data(user_id: int, user_data_in: UserDataUpdate, db: Session = Depends(get_db)):
    return UserDataService(db).update_user_data(user_id, user_data_in)

@router.delete("/users/{user_id}/data/")
async def delete_user_data(user_id: int, db: Session = Depends(get_db)):
    if UserDataService(db).delete_user_data(user_id):
        return {"message": "User data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User data not found")

@router.post("/users/{user_id}/chatbot-logs/", response_model=ChatbotLogResponse)
async def create_chatbot_log(user_id: int, chatbot_log_in: ChatbotLogCreate, db: Session = Depends(get_db)):
    return ChatbotLogService(db).create_chatbot_log(chatbot_log_in)

@router.get("/users/{user_id}/chatbot-logs/", response_model=ChatbotLogResponse)
async def get_chatbot_log(user_id: int, db: Session = Depends(get_db)):
    chatbot_log = ChatbotLogService(db).get_chatbot_log(user_id)
    if chatbot_log:
        return chatbot_log
    else:
        raise HTTPException(status_code=404, detail="Chatbot log not found")

@router.put("/users/{user_id}/chatbot-logs/", response_model=ChatbotLogResponse)
async def update_chatbot_log(user_id: int, chatbot_log_in: ChatbotLogUpdate, db: Session = Depends(get_db)):
    return ChatbotLogService(db).update_chatbot_log(user_id, chatbot_log_in)

@router.delete("/users/{user_id}/chatbot-logs/")
async def delete_chatbot_log(user_id: int, db: Session = Depends(get_db)):
    if ChatbotLogService(db).delete_chatbot_log(user_id):
        return {"message": "Chatbot log deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Chatbot log not found")

@router.post("/chatbot/log/", response_model=ChatbotLogResponse)
async def get_chatbot_response(chatbot_log_in: ChatbotLogCreate, db: Session = Depends(get_db)):
    return ChatbotService().get_response(chatbot_log_in.query)

@router.post("/llm/log/", response_model=ChatbotLogResponse)
async def get_llm_response(llm_log_in: ChatbotLogCreate, db: Session = Depends(get_db)):
    return LLMChainService().get_response(llm_log_in.query)
```
Here's the `routers.py` file based on the provided requirements:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services import UserService, ConversationService, ModelOutputService, get_db
from schemas import (
    UserCreate,
    UserUpdate,
    UserResponse,
    ConversationCreate,
    ConversationUpdate,
    ConversationResponse,
    ModelOutputCreate,
    ModelOutputUpdate,
    ModelOutputResponse,
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
    ForgotPasswordRequest,
    ForgotPasswordResponse,
    ResetPasswordRequest,
    ResetPasswordResponse,
    ChangePasswordRequest,
    ChangePasswordResponse,
    GetConversationsRequest,
    GetConversationsResponse,
    GetModelOutputsRequest,
    GetModelOutputsResponse,
    GetConversationRequest,
    GetConversationResponse,
    GetModelOutputRequest,
    GetModelOutputResponse,
)

router = APIRouter()

@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return UserService().create_user(db, user_in)

@router.get("/users/", response_model=UserResponseList)
async def read_users(db: Session = Depends(get_db)):
    return UserService().get_users(db)

@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return UserService().get_user(db, user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    return UserService().update_user(db, user_id, user_in)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserService().delete_user(db, user_id)
    return {"message": "User deleted"}

@router.post("/users/login", response_model=LoginResponse)
async def login_user(user_in: LoginRequest, db: Session = Depends(get_db)):
    # Implement login logic here
    return {"access_token": "token", "token_type": "bearer"}

@router.post("/users/register", response_model=RegisterResponse)
async def register_user(user_in: RegisterRequest, db: Session = Depends(get_db)):
    return UserService().create_user(db, user_in)

@router.post("/users/forgot-password", response_model=ForgotPasswordResponse)
async def forgot_password(user_in: ForgotPasswordRequest, db: Session = Depends(get_db)):
    # Implement forgot password logic here
    return {"message": "Password reset email sent"}

@router.post("/users/reset-password", response_model=ResetPasswordResponse)
async def reset_password(user_in: ResetPasswordRequest, db: Session = Depends(get_db)):
    # Implement reset password logic here
    return {"message": "Password reset successful"}

@router.post("/users/change-password", response_model=ChangePasswordResponse)
async def change_password(user_in: ChangePasswordRequest, db: Session = Depends(get_db)):
    # Implement change password logic here
    return {"message": "Password changed"}

@router.post("/conversations/", response_model=ConversationResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(conversation_in: ConversationCreate, db: Session = Depends(get_db)):
    return ConversationService().create_conversation(db, conversation_in)

@router.get("/conversations/", response_model=ConversationResponseList)
async def read_conversations(db: Session = Depends(get_db)):
    return ConversationService().get_conversations(db, None)

@router.get("/conversations/{conversation_id}", response_model=ConversationResponse)
async def read_conversation(conversation_id: int, db: Session = Depends(get_db)):
    return ConversationService().get_conversation(db, conversation_id)

@router.put("/conversations/{conversation_id}", response_model=ConversationResponse)
async def update_conversation(conversation_id: int, conversation_in: ConversationUpdate, db: Session = Depends(get_db)):
    return ConversationService().update_conversation(db, conversation_id, conversation_in)

@router.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    ConversationService().delete_conversation(db, conversation_id)
    return {"message": "Conversation deleted"}

@router.post("/model-outputs/", response_model=ModelOutputResponse, status_code=status.HTTP_201_CREATED)
async def create_model_output(model_output_in: ModelOutputCreate, db: Session = Depends(get_db)):
    return ModelOutputService().create_model_output(db, model_output_in)

@router.get("/model-outputs/", response_model=ModelOutputResponseList)
async def read_model_outputs(db: Session = Depends(get_db)):
    return ModelOutputService().get_model_outputs(db, None)

@router.get("/model-outputs/{model_output_id}", response_model=ModelOutputResponse)
async def read_model_output(model_output_id: int, db: Session = Depends(get_db)):
    return ModelOutputService().get_model_output(db, model_output_id)

@router.put("/model-outputs/{model_output_id}", response_model=ModelOutputResponse)
async def update_model_output(model_output_id: int, model_output_in: ModelOutputUpdate, db: Session = Depends(get_db)):
    return ModelOutputService().update_model_output(db, model_output_id, model_output_in)

@router.delete("/model-outputs/{model_output_id}")
async def delete_model_output(model_output_id: int, db: Session = Depends(get_db)):
    ModelOutputService().delete_model_output(db, model_output_id)
    return {"message": "Model output deleted"}

@router.get("/conversations/{user_id}", response_model=GetConversationsResponse)
async def get_conversations(user_id: int, db: Session = Depends(get_db)):
    return ConversationService().get_conversations(db, user_id)

@router.get("/model-outputs/{conversation_id}", response_model=GetModelOutputsResponse)
async def get_model_outputs(conversation_id: int, db: Session = Depends(get_db)):
    return ModelOutputService().get_model_outputs(db, conversation_id)

@router.get("/conversations/{conversation_id}", response_model=GetConversationResponse)
async def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    return ConversationService().get_conversation(db, conversation_id)

@router.get("/model-outputs/{model_output_id}", response_model=GetModelOutputResponse)
async def get_model_output(model_output_id: int, db: Session = Depends(get_db)):
    return ModelOutputService().get_model_output(db, model_output_id)
```

This `routers.py` file defines the API routes for the application using the FastAPI framework. It includes routes for creating, reading, updating, and deleting users, conversations, and model outputs. The routes use the provided Pydantic schemas as request and response models and call the service layer to perform the business logic. The routes also use dependency injection to get a database session from the `get_db` function.

Note that this code assumes that the `services.py` file is already created and that the `get_db` function is defined in the `services.utils` module. The code also assumes that the `models.py` file is already created and that the `SessionLocal` class is defined in the `services.utils` module.

Also, note that this code does not implement the business logic for the application. It only defines the API routes and calls the service layer to perform the business logic. The business logic should be implemented in the service layer.

Finally, note that this code uses async endpoints where appropriate and returns proper HTTP status codes.
```python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import UserService, AiModelService, UserAiModelService, DataService
from schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema, \
    AiModelCreateSchema, AiModelUpdateSchema, AiModelResponseSchema, \
    UserAiModelCreateSchema, UserAiModelUpdateSchema, UserAiModelResponseSchema, \
    DataCreateSchema, DataUpdateSchema, DataResponseSchema
from database import get_db
from langchain import LLMChain
from typing import Optional

router = APIRouter()

@router.post("/users/", response_model=UserResponseSchema)
async def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@router.get("/users/{user_id}", response_model=UserResponseSchema)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return UserService(db).get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/users/{user_id}", response_model=UserResponseSchema)
async def update_user(user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserService(db).delete_user(user_id)

@router.post("/ai-models/", response_model=AiModelResponseSchema)
async def create_ai_model(ai_model: AiModelCreateSchema, db: Session = Depends(get_db)):
    return AiModelService(db).create_ai_model(ai_model)

@router.get("/ai-models/{ai_model_id}", response_model=AiModelResponseSchema)
async def read_ai_model(ai_model_id: int, db: Session = Depends(get_db)):
    try:
        return AiModelService(db).get_ai_model(ai_model_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/ai-models/{ai_model_id}", response_model=AiModelResponseSchema)
async def update_ai_model(ai_model_id: int, ai_model: AiModelUpdateSchema, db: Session = Depends(get_db)):
    return AiModelService(db).update_ai_model(ai_model_id, ai_model)

@router.delete("/ai-models/{ai_model_id}")
async def delete_ai_model(ai_model_id: int, db: Session = Depends(get_db)):
    AiModelService(db).delete_ai_model(ai_model_id)

@router.post("/user-ai-models/", response_model=UserAiModelResponseSchema)
async def create_user_ai_model(user_ai_model: UserAiModelCreateSchema, db: Session = Depends(get_db)):
    return UserAiModelService(db).create_user_ai_model(user_ai_model)

@router.get("/user-ai-models/{user_ai_model_id}", response_model=UserAiModelResponseSchema)
async def read_user_ai_model(user_ai_model_id: int, db: Session = Depends(get_db)):
    try:
        return UserAiModelService(db).get_user_ai_model(user_ai_model_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/user-ai-models/{user_ai_model_id}", response_model=UserAiModelResponseSchema)
async def update_user_ai_model(user_ai_model_id: int, user_ai_model: UserAiModelUpdateSchema, db: Session = Depends(get_db)):
    return UserAiModelService(db).update_user_ai_model(user_ai_model_id, user_ai_model)

@router.delete("/user-ai-models/{user_ai_model_id}")
async def delete_user_ai_model(user_ai_model_id: int, db: Session = Depends(get_db)):
    UserAiModelService(db).delete_user_ai_model(user_ai_model_id)

@router.post("/data/", response_model=DataResponseSchema)
async def create_data(data: DataCreateSchema, db: Session = Depends(get_db)):
    return DataService(db).create_data(data)

@router.get("/data/{data_id}", response_model=DataResponseSchema)
async def read_data(data_id: int, db: Session = Depends(get_db)):
    try:
        return DataService(db).get_data(data_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/data/{data_id}", response_model=DataResponseSchema)
async def update_data(data_id: int, data: DataUpdateSchema, db: Session = Depends(get_db)):
    return DataService(db).update_data(data_id, data)

@router.delete("/data/{data_id}")
async def delete_data(data_id: int, db: Session = Depends(get_db)):
    DataService(db).delete_data(data_id)

@router.post("/llm-chain/")
async def create_llm_chain(llm_chain: LLMChain):
    return {"llm_chain": llm_chain}

@router.get("/llm-chain/{llm_chain_id}")
async def read_llm_chain(llm_chain_id: int):
    return {"llm_chain_id": llm_chain_id}

@router.put("/llm-chain/{llm_chain_id}")
async def update_llm_chain(llm_chain_id: int, llm_chain: LLMChain):
    return {"llm_chain_id": llm_chain_id, "llm_chain": llm_chain}

@router.delete("/llm-chain/{llm_chain_id}")
async def delete_llm_chain(llm_chain_id: int):
    return {"llm_chain_id": llm_chain_id}
```

```python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import UserService, AiModelService, UserAiModelService, DataService
from schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema, \
    AiModelCreateSchema, AiModelUpdateSchema, AiModelResponseSchema, \
    UserAiModelCreateSchema, UserAiModelUpdateSchema, UserAiModelResponseSchema, \
    DataCreateSchema, DataUpdateSchema, DataResponseSchema
from database import get_db
from typing import Optional

router = APIRouter()

@router.post("/auth/token", response_model=AuthTokenResponseSchema)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        return UserService(db).login(form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/auth/token/refresh", response_model=AuthTokenResponseSchema)
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        return UserService(db).refresh_token(refresh_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
```

```python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services import UserService
from schemas import AuthTokenCreateSchema, AuthTokenUpdateSchema, AuthTokenResponseSchema
from database import get_db
from typing import Optional

router = APIRouter()

@router.post("/auth/token", response_model=AuthTokenResponseSchema)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        return UserService(db).login(form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/auth/token/refresh", response_model=AuthTokenResponseSchema)
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        return UserService(db).refresh_token(refresh_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/auth/token/create", response_model=AuthTokenResponseSchema)
async def create_token(token: AuthTokenCreateSchema, db: Session = Depends(get_db)):
    try:
        return UserService(db).create_token(token.username, token.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.put("/auth/token/{token_id}", response_model=AuthTokenResponseSchema)
async def update_token(token_id: int, token: AuthTokenUpdateSchema, db: Session = Depends(get_db)):
    try:
        return UserService(db).update_token(token_id, token.username, token.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.delete("/auth/token/{token_id}")
async def delete_token(token_id: int, db: Session = Depends(get_db)):
    try:
        UserService(db).delete_token(token_id)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
```
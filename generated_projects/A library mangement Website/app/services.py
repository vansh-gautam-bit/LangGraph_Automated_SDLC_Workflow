```python
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional
from services.models import User, AiModel, UserAiModel, Data
from services.schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema, \
    AiModelCreateSchema, AiModelUpdateSchema, AiModelResponseSchema, \
    UserAiModelCreateSchema, UserAiModelUpdateSchema, UserAiModelResponseSchema, \
    DataCreateSchema, DataUpdateSchema, DataResponseSchema

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> UserResponseSchema:
        user = self.db.get(User, user_id)
        if user:
            return UserResponseSchema(id=user.id, username=user.username, email=user.email)
        else:
            raise Exception(f"User with ID {user_id} not found")

    def create_user(self, user: UserCreateSchema) -> UserResponseSchema:
        new_user = User(username=user.username, email=user.email, password=user.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return UserResponseSchema(id=new_user.id, username=new_user.username, email=new_user.email)

    def update_user(self, user_id: int, user: UserUpdateSchema) -> UserResponseSchema:
        existing_user = self.db.get(User, user_id)
        if existing_user:
            if user.username:
                existing_user.username = user.username
            if user.email:
                existing_user.email = user.email
            if user.password:
                existing_user.password = user.password
            self.db.commit()
            self.db.refresh(existing_user)
            return UserResponseSchema(id=existing_user.id, username=existing_user.username, email=existing_user.email)
        else:
            raise Exception(f"User with ID {user_id} not found")

    def delete_user(self, user_id: int):
        user = self.db.get(User, user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        else:
            raise Exception(f"User with ID {user_id} not found")


class AiModelService:
    def __init__(self, db: Session):
        self.db = db

    def get_ai_model(self, ai_model_id: int) -> AiModelResponseSchema:
        ai_model = self.db.get(AiModel, ai_model_id)
        if ai_model:
            return AiModelResponseSchema(id=ai_model.id, name=ai_model.name, description=ai_model.description)
        else:
            raise Exception(f"AI Model with ID {ai_model_id} not found")

    def create_ai_model(self, ai_model: AiModelCreateSchema) -> AiModelResponseSchema:
        new_ai_model = AiModel(name=ai_model.name, description=ai_model.description)
        self.db.add(new_ai_model)
        self.db.commit()
        self.db.refresh(new_ai_model)
        return AiModelResponseSchema(id=new_ai_model.id, name=new_ai_model.name, description=new_ai_model.description)

    def update_ai_model(self, ai_model_id: int, ai_model: AiModelUpdateSchema) -> AiModelResponseSchema:
        existing_ai_model = self.db.get(AiModel, ai_model_id)
        if existing_ai_model:
            if ai_model.name:
                existing_ai_model.name = ai_model.name
            if ai_model.description:
                existing_ai_model.description = ai_model.description
            self.db.commit()
            self.db.refresh(existing_ai_model)
            return AiModelResponseSchema(id=existing_ai_model.id, name=existing_ai_model.name, description=existing_ai_model.description)
        else:
            raise Exception(f"AI Model with ID {ai_model_id} not found")

    def delete_ai_model(self, ai_model_id: int):
        ai_model = self.db.get(AiModel, ai_model_id)
        if ai_model:
            self.db.delete(ai_model)
            self.db.commit()
        else:
            raise Exception(f"AI Model with ID {ai_model_id} not found")


class UserAiModelService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_ai_model(self, user_ai_model_id: int) -> UserAiModelResponseSchema:
        user_ai_model = self.db.get(UserAiModel, user_ai_model_id)
        if user_ai_model:
            return UserAiModelResponseSchema(id=user_ai_model.id, user_id=user_ai_model.user_id, ai_model_id=user_ai_model.ai_model_id)
        else:
            raise Exception(f"User-AI Model association with ID {user_ai_model_id} not found")

    def create_user_ai_model(self, user_ai_model: UserAiModelCreateSchema) -> UserAiModelResponseSchema:
        new_user_ai_model = UserAiModel(user_id=user_ai_model.user_id, ai_model_id=user_ai_model.ai_model_id)
        self.db.add(new_user_ai_model)
        self.db.commit()
        self.db.refresh(new_user_ai_model)
        return UserAiModelResponseSchema(id=new_user_ai_model.id, user_id=new_user_ai_model.user_id, ai_model_id=new_user_ai_model.ai_model_id)

    def update_user_ai_model(self, user_ai_model_id: int, user_ai_model: UserAiModelUpdateSchema) -> UserAiModelResponseSchema:
        existing_user_ai_model = self.db.get(UserAiModel, user_ai_model_id)
        if existing_user_ai_model:
            if user_ai_model.user_id:
                existing_user_ai_model.user_id = user_ai_model.user_id
            if user_ai_model.ai_model_id:
                existing_user_ai_model.ai_model_id = user_ai_model.ai_model_id
            self.db.commit()
            self.db.refresh(existing_user_ai_model)
            return UserAiModelResponseSchema(id=existing_user_ai_model.id, user_id=existing_user_ai_model.user_id, ai_model_id=existing_user_ai_model.ai_model_id)
        else:
            raise Exception(f"User-AI Model association with ID {user_ai_model_id} not found")

    def delete_user_ai_model(self, user_ai_model_id: int):
        user_ai_model = self.db.get(UserAiModel, user_ai_model_id)
        if user_ai_model:
            self.db.delete(user_ai_model)
            self.db.commit()
        else:
            raise Exception(f"User-AI Model association with ID {user_ai_model_id} not found")


class DataService:
    def __init__(self, db: Session):
        self.db = db

    def get_data(self, data_id: int) -> DataResponseSchema:
        data = self.db.get(Data, data_id)
        if data:
            return DataResponseSchema(id=data.id, user_id=data.user_id, ai_model_id=data.ai_model_id, data=data.data)
        else:
            raise Exception(f"Data with ID {data_id} not found")

    def create_data(self, data: DataCreateSchema) -> DataResponseSchema:
        new_data = Data(user_id=data.user_id, ai_model_id=data.ai_model_id, data=data.data)
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return DataResponseSchema(id=new_data.id, user_id=new_data.user_id, ai_model_id=new_data.ai_model_id, data=new_data.data)

    def update_data(self, data_id: int, data: DataUpdateSchema) -> DataResponseSchema:
        existing_data = self.db.get(Data, data_id)
        if existing_data:
            if data.user_id:
                existing_data.user_id = data.user_id
            if data.ai_model_id:
                existing_data.ai_model_id = data.ai_model_id
            if data.data:
                existing_data.data = data.data
            self.db.commit()
            self.db.refresh(existing_data)
            return DataResponseSchema(id=existing_data.id, user_id=existing_data.user_id, ai_model_id=existing_data.ai_model_id, data=existing_data.data)
        else:
            raise Exception(f"Data with ID {data_id} not found")

    def delete_data(self, data_id: int):
        data = self.db.get(Data, data_id)
        if data:
            self.db.delete(data)
            self.db.commit()
        else:
            raise Exception(f"Data with ID {data_id} not found")
```
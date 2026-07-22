```python
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class UserCreateSchema(BaseModel):
    """Schema for creating a new user."""
    username: str = Field(..., title="Username", description="The username of the user.")
    email: str = Field(..., title="Email", description="The email of the user.")
    password: str = Field(..., title="Password", description="The password of the user.")

class UserUpdateSchema(BaseModel):
    """Schema for updating an existing user."""
    username: Optional[str] = Field(None, title="Username", description="The username of the user.")
    email: Optional[str] = Field(None, title="Email", description="The email of the user.")
    password: Optional[str] = Field(None, title="Password", description="The password of the user.")

class UserResponseSchema(BaseModel):
    """Schema for a user response."""
    id: int
    username: str
    email: str

class AiModelCreateSchema(BaseModel):
    """Schema for creating a new AI model."""
    name: str = Field(..., title="Name", description="The name of the AI model.")
    description: str = Field(..., title="Description", description="The description of the AI model.")

class AiModelUpdateSchema(BaseModel):
    """Schema for updating an existing AI model."""
    name: Optional[str] = Field(None, title="Name", description="The name of the AI model.")
    description: Optional[str] = Field(None, title="Description", description="The description of the AI model.")

class AiModelResponseSchema(BaseModel):
    """Schema for an AI model response."""
    id: int
    name: str
    description: str

class UserAiModelCreateSchema(BaseModel):
    """Schema for creating a new user-AI model association."""
    user_id: int
    ai_model_id: int

class UserAiModelUpdateSchema(BaseModel):
    """Schema for updating an existing user-AI model association."""
    user_id: Optional[int] = Field(None, title="User ID", description="The ID of the user.")
    ai_model_id: Optional[int] = Field(None, title="AI Model ID", description="The ID of the AI model.")

class UserAiModelResponseSchema(BaseModel):
    """Schema for a user-AI model association response."""
    id: int
    user_id: int
    ai_model_id: int

class DataCreateSchema(BaseModel):
    """Schema for creating new data."""
    user_id: int
    ai_model_id: int
    data: str

class DataUpdateSchema(BaseModel):
    """Schema for updating existing data."""
    user_id: Optional[int] = Field(None, title="User ID", description="The ID of the user.")
    ai_model_id: Optional[int] = Field(None, title="AI Model ID", description="The ID of the AI model.")
    data: Optional[str] = Field(None, title="Data", description="The data.")

class DataResponseSchema(BaseModel):
    """Schema for a data response."""
    id: int
    user_id: int
    ai_model_id: int
    data: str

class AuthTokenSchema(BaseModel):
    """Schema for an authentication token."""
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    scope: str

class AuthTokenCreateSchema(BaseModel):
    """Schema for creating a new authentication token."""
    username: str
    password: str

class AuthTokenUpdateSchema(BaseModel):
    """Schema for updating an existing authentication token."""
    username: Optional[str] = Field(None, title="Username", description="The username of the user.")
    password: Optional[str] = Field(None, title="Password", description="The password of the user.")

class AuthTokenResponseSchema(BaseModel):
    """Schema for an authentication token response."""
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    scope: str
```

This `schemas.py` file defines the request and response schemas for the API endpoints using Pydantic v2. It includes separate schemas for creating, updating, and responding to user, AI model, user-AI model association, data, authentication token, and other related data. The schemas are designed to be clean, maintainable, and follow FastAPI best practices.
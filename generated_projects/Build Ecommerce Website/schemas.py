```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """User create schema."""
    username: str = Field(..., title="Username", max_length=50)
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password", min_length=8)

class UserUpdate(BaseModel):
    """User update schema."""
    username: Optional[str] = Field(None, title="Username", max_length=50)
    email: Optional[EmailStr] = Field(None, title="Email")
    password: Optional[str] = Field(None, title="Password", min_length=8)

class UserResponse(BaseModel):
    """User response schema."""
    id: int
    username: str
    email: EmailStr
    created_at: datetime

class DataCreate(BaseModel):
    """Data create schema."""
    data: dict = Field(..., title="Data")

class DataUpdate(BaseModel):
    """Data update schema."""
    data: Optional[dict] = Field(None, title="Data")

class DataResponse(BaseModel):
    """Data response schema."""
    id: int
    data: dict
    created_at: datetime

class Token(BaseModel):
    """Token schema."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Token data schema."""
    username: Optional[str] = None
```

This code defines the request and response schemas for the user and data models using pydantic v2. It includes separate create, update, and response schemas for each model, and uses optional fields where necessary. The code also includes proper type hints, descriptive class names, and follows FastAPI best practices.
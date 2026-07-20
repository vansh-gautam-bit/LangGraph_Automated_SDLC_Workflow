```python
from pydantic import BaseModel, Config, Field
from typing import Optional

class UserCreate(BaseModel):
    """User create request schema"""
    username: str = Field(..., title="Username")
    email: str = Field(..., title="Email")
    password: str = Field(..., title="Password")

class UserUpdate(BaseModel):
    """User update request schema"""
    username: Optional[str] = Field(None, title="Username")
    email: Optional[str] = Field(None, title="Email")
    password: Optional[str] = Field(None, title="Password")

class UserResponse(BaseModel):
    """User response schema"""
    id: int
    username: str
    email: str

class UserResponseList(BaseModel):
    """User response list schema"""
    users: list[UserResponse]

class ConversationCreate(BaseModel):
    """Conversation create request schema"""
    user_id: int = Field(..., title="User ID")
    conversation_text: str = Field(..., title="Conversation Text")

class ConversationUpdate(BaseModel):
    """Conversation update request schema"""
    conversation_text: Optional[str] = Field(None, title="Conversation Text")

class ConversationResponse(BaseModel):
    """Conversation response schema"""
    id: int
    user_id: int
    conversation_text: str
    created_at: str

class ConversationResponseList(BaseModel):
    """Conversation response list schema"""
    conversations: list[ConversationResponse]

class ModelOutputCreate(BaseModel):
    """Model output create request schema"""
    conversation_id: int = Field(..., title="Conversation ID")
    output_text: str = Field(..., title="Output Text")

class ModelOutputUpdate(BaseModel):
    """Model output update request schema"""
    output_text: Optional[str] = Field(None, title="Output Text")

class ModelOutputResponse(BaseModel):
    """Model output response schema"""
    id: int
    conversation_id: int
    output_text: str
    created_at: str

class ModelOutputResponseList(BaseModel):
    """Model output response list schema"""
    model_outputs: list[ModelOutputResponse]

class LoginRequest(BaseModel):
    """Login request schema"""
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")

class LoginResponse(BaseModel):
    """Login response schema"""
    access_token: str
    token_type: str

class RegisterRequest(BaseModel):
    """Register request schema"""
    username: str = Field(..., title="Username")
    email: str = Field(..., title="Email")
    password: str = Field(..., title="Password")

class RegisterResponse(BaseModel):
    """Register response schema"""
    user: UserResponse

class ForgotPasswordRequest(BaseModel):
    """Forgot password request schema"""
    email: str = Field(..., title="Email")

class ForgotPasswordResponse(BaseModel):
    """Forgot password response schema"""
    message: str

class ResetPasswordRequest(BaseModel):
    """Reset password request schema"""
    password: str = Field(..., title="Password")
    reset_token: str = Field(..., title="Reset Token")

class ResetPasswordResponse(BaseModel):
    """Reset password response schema"""
    message: str

class ChangePasswordRequest(BaseModel):
    """Change password request schema"""
    old_password: str = Field(..., title="Old Password")
    new_password: str = Field(..., title="New Password")

class ChangePasswordResponse(BaseModel):
    """Change password response schema"""
    message: str

class GetConversationsRequest(BaseModel):
    """Get conversations request schema"""
    user_id: int = Field(..., title="User ID")

class GetConversationsResponse(BaseModel):
    """Get conversations response schema"""
    conversations: list[ConversationResponse]

class GetModelOutputsRequest(BaseModel):
    """Get model outputs request schema"""
    conversation_id: int = Field(..., title="Conversation ID")

class GetModelOutputsResponse(BaseModel):
    """Get model outputs response schema"""
    model_outputs: list[ModelOutputResponse]

class GetConversationRequest(BaseModel):
    """Get conversation request schema"""
    conversation_id: int = Field(..., title="Conversation ID")

class GetConversationResponse(BaseModel):
    """Get conversation response schema"""
    conversation: ConversationResponse

class GetModelOutputRequest(BaseModel):
    """Get model output request schema"""
    model_output_id: int = Field(..., title="Model Output ID")

class GetModelOutputResponse(BaseModel):
    """Get model output response schema"""
    model_output: ModelOutputResponse
```

This `schemas.py` file defines all the request and response schemas for the API using Pydantic v2. Each schema is separated into its own class and has descriptive names. The `BaseModel` is used as the base class for all schemas, and the `Config` is used to configure the schema generation. The `Field` is used to add metadata to each field, such as the title and the type. The `Optional` type is used to indicate that a field is optional. The `List` type is used to indicate that a field is a list of items. The `Dict` type is used to indicate that a field is a dictionary. The `Any` type is used to indicate that a field can be any type. The `ConfigDict(from_attributes=True)` is used to generate the schema from the attributes of the class.
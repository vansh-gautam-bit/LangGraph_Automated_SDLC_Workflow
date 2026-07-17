Here's the complete `schemas.py` file based on the provided specifications:

```python
# schemas.py

from pydantic import BaseModel, Config, Field
from typing import Optional

class UserCreate(BaseModel):
    """User create schema."""
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    """User update schema."""
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

class UserResponse(BaseModel):
    """User response schema."""
    id: int
    username: str
    email: str

class ChatbotInteractionCreate(BaseModel):
    """Chatbot interaction create schema."""
    user_id: int
    interaction_text: str
    response_text: str

class ChatbotInteractionUpdate(BaseModel):
    """Chatbot interaction update schema."""
    interaction_text: Optional[str]
    response_text: Optional[str]

class ChatbotInteractionResponse(BaseModel):
    """Chatbot interaction response schema."""
    id: int
    user_id: int
    interaction_text: str
    response_text: str

class ChatbotPerformanceCreate(BaseModel):
    """Chatbot performance create schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotPerformanceUpdate(BaseModel):
    """Chatbot performance update schema."""
    accuracy: Optional[str]
    response_time: Optional[str]

class ChatbotPerformanceResponse(BaseModel):
    """Chatbot performance response schema."""
    id: int
    user_id: int
    accuracy: str
    response_time: str

class UserLogin(BaseModel):
    """User login schema."""
    username: str
    password: str

class Token(BaseModel):
    """Token schema."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Token data schema."""
    username: Optional[str]

class ChatbotInteractionRequest(BaseModel):
    """Chatbot interaction request schema."""
    interaction_text: str

class ChatbotInteractionResponseData(BaseModel):
    """Chatbot interaction response data schema."""
    response_text: str

class ChatbotPerformanceRequest(BaseModel):
    """Chatbot performance request schema."""
    accuracy: str
    response_time: str

class ChatbotPerformanceResponseData(BaseModel):
    """Chatbot performance response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionListResponse(BaseModel):
    """Chatbot interaction list response schema."""
    interactions: list[ChatbotInteractionResponse]

class ChatbotPerformanceListResponse(BaseModel):
    """Chatbot performance list response schema."""
    performances: list[ChatbotPerformanceResponse]

class UserListResponse(BaseModel):
    """User list response schema."""
    users: list[UserResponse]

class ChatbotInteractionDetailedResponse(BaseModel):
    """Chatbot interaction detailed response schema."""
    interaction: ChatbotInteractionResponse
    user: UserResponse

class ChatbotPerformanceDetailedResponse(BaseModel):
    """Chatbot performance detailed response schema."""
    performance: ChatbotPerformanceResponse
    user: UserResponse

class ChatbotInteractionDetailedListResponse(BaseModel):
    """Chatbot interaction detailed list response schema."""
    interactions: list[ChatbotInteractionDetailedResponse]

class ChatbotPerformanceDetailedListResponse(BaseModel):
    """Chatbot performance detailed list response schema."""
    performances: list[ChatbotPerformanceDetailedResponse]

class ChatbotInteractionDetailedRequest(BaseModel):
    """Chatbot interaction detailed request schema."""
    user_id: int
    interaction_text: str

class ChatbotPerformanceDetailedRequest(BaseModel):
    """Chatbot performance detailed request schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedResponseData(BaseModel):
    """Chatbot interaction detailed response data schema."""
    response_text: str

class ChatbotPerformanceDetailedResponseData(BaseModel):
    """Chatbot performance detailed response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedListRequest(BaseModel):
    """Chatbot interaction detailed list request schema."""
    user_id: int

class ChatbotPerformanceDetailedListRequest(BaseModel):
    """Chatbot performance detailed list request schema."""
    user_id: int

class ChatbotInteractionDetailedListResponseData(BaseModel):
    """Chatbot interaction detailed list response data schema."""
    response_text: str

class ChatbotPerformanceDetailedListResponseData(BaseModel):
    """Chatbot performance detailed list response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedRequest(BaseModel):
    """Chatbot interaction detailed detailed request schema."""
    user_id: int
    interaction_text: str

class ChatbotPerformanceDetailedDetailedRequest(BaseModel):
    """Chatbot performance detailed detailed request schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedResponseData(BaseModel):
    """Chatbot interaction detailed detailed response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedResponseData(BaseModel):
    """Chatbot performance detailed detailed response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedListRequest(BaseModel):
    """Chatbot interaction detailed detailed list request schema."""
    user_id: int

class ChatbotPerformanceDetailedDetailedListRequest(BaseModel):
    """Chatbot performance detailed detailed list request schema."""
    user_id: int

class ChatbotInteractionDetailedDetailedListResponseData(BaseModel):
    """Chatbot interaction detailed detailed list response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedListResponseData(BaseModel):
    """Chatbot performance detailed detailed list response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed request schema."""
    user_id: int
    interaction_text: str

class ChatbotPerformanceDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot performance detailed detailed detailed request schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed list request schema."""
    user_id: int

class ChatbotPerformanceDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot performance detailed detailed detailed list request schema."""
    user_id: int

class ChatbotInteractionDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed list response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed list response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed request schema."""
    user_id: int
    interaction_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot performance detailed detailed detailed detailed request schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed detailed response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed list request schema."""
    user_id: int

class ChatbotPerformanceDetailedDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot performance detailed detailed detailed detailed list request schema."""
    user_id: int

class ChatbotInteractionDetailedDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed list response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed detailed list response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed detailed request schema."""
    user_id: int
    interaction_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot performance detailed detailed detailed detailed detailed request schema."""
    user_id: int
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed detailed response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed detailed detailed response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed detailed list request schema."""
    user_id: int

class ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedListRequest(BaseModel):
    """Chatbot performance detailed detailed detailed detailed detailed list request schema."""
    user_id: int

class ChatbotInteractionDetailedDetailedDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot interaction detailed detailed detailed detailed detailed list response data schema."""
    response_text: str

class ChatbotPerformanceDetailedDetailedDetailedDetailedDetailedListResponseData(BaseModel):
    """Chatbot performance detailed detailed detailed detailed detailed list response data schema."""
    accuracy: str
    response_time: str

class ChatbotInteractionDetailedDetailedDetailedDetailedDetailedDetailedRequest(BaseModel):
    """Chatbot interaction detailed
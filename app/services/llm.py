from langchain_openrouter import ChatOpenRouter

from app.config import settings

llm = ChatOpenRouter(
    model=settings.OPENROUTER_MODEL,
    api_key=settings.OPENROUTER_API_KEY,
    temperature=0.2,
)
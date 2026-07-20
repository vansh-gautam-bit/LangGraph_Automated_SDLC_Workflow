from mem0 import Memory
from app.config import settings

memory = Memory.from_config(
    {
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "collection_name": "sdlc_memory",
                "path": "C:/Users/vansh/.mem0/qdrant",
                "embedding_model_dims": 768,
            },
        },

        "llm": {
            "provider": "openai",
            "config": {
                "api_key": settings.OPENROUTER_API_KEY,
                "openai_base_url": "https://openrouter.ai/api/v1",
                "model": settings.OPENROUTER_MODEL,
            },
        },

        "embedder": {
            "provider": "gemini",
            "config": {
                "api_key": settings.GOOGLE_API_KEY,
                "model": "models/gemini-embedding-001",
            },
        },
    }
)
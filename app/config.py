from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    GOOGLE_API_KEY: str
    GOOGLE_MODEL: str
    GOOGLE_EMBEDDING_MODEL: str = "models/gemini-embedding-001"

    DATABASE_URL: str

    MEM0_API_KEY: str

    LANGSMITH_API_KEY:str
    LANGSMITH_TRACING: bool =False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
settings = Settings()

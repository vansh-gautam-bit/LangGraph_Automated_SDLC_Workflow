from fastapi import FastAPI
import app.langsmith
from app.router import router

app = FastAPI(
    title="LangGraph Automated SDLC Workflow"
)

app.include_router(router)
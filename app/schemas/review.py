from pydantic import BaseModel

class ReviewRequest(BaseModel):
    thread_id: str
    decision: str
    feedback: str | None = None

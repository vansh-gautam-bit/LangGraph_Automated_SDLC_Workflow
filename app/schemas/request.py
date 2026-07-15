from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    project_name: str
    requirements: str
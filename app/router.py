from fastapi import APIRouter
from app.schemas.request import WorkflowRequest
from app.graph import graph

router =APIRouter()

@router.post("/workflow/start")
def start_workflow(request: WorkflowRequest):

    initial_state = {

        "project_name": request.project_name,

        "user_requirements": request.requirements,

        "product_owner_artifact": None,

        "architecture_artifact": None,

        "developer_artifact": None,

        "review_artifact": None,

        "security_artifact": None,

        "testing_artifact": None,

        "qa_artifact": None,

        "depoyment_artifact": None,

        "project_files": {},

        "history": [],

        "current_stage": "Requirements"
    }

    result = graph.invoke(initial_state)

    return result

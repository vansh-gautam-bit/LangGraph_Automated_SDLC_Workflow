from fastapi import APIRouter
from app.schemas.request import WorkflowRequest
from app.graph import graph
import uuid
from langgraph.types import Command
from app.schemas.review import ReviewRequest

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

        "deployment_artifact": None,

        "review_decision": None,

        "user_feedback": "",

        "project_files": {},

        "history": [],

        "current_stage": "Requirements"
    }

    thread_id = str(uuid.uuid4())

    config = {
        "configurable": {
            "thread_id":thread_id
        }
    }

    try:
        result = graph.invoke(
            initial_state,
            config=config
        )

        return {
            "thread_id": thread_id,
            "result": result
        }

    except Exception as e:
        import traceback

        print("\n" + "=" * 80)
        traceback.print_exc()
        print("=" * 80 + "\n")

        return {
            "error": str(e)
        }

@router.post("/workflow/review")
def review_workflow(request: ReviewRequest):

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    result = graph.invoke(
        Command(
            resume={
                "decision":request.decision,
                "feedback": request.feedback
            }
        ),
        config=config
    )

    return result

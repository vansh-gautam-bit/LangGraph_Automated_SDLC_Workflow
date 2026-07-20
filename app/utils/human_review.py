from langgraph.types import interrupt

def human_review(stage: str, artifact: str):

    return interrupt(
        {
            "stage": stage,
            "artifact": artifact,
            "message": f"review the {stage} artifact and approve or provide feedback"
        }
    )
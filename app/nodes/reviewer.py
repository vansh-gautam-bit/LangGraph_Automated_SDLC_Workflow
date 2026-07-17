from pathlib import Path

from app.prompts.reviewer import REVIEWER_PROMPT
from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage
from app.utils.file_review import review_project_files


def reviewer_node(state):

    report = review_project_files(
        state["generated_project_path"],
        REVIEWER_PROMPT
    )

    return complete_stage(
        state=state,
        artifact_name="review_artifact",
        artifact=report,
        next_stage="Security",
        message="✅ Review completed."
    )
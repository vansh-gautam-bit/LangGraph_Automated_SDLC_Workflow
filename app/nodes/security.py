from pathlib import Path

from app.prompts.security import SECURITY_PROMPT
from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage
from app.utils.file_review import review_project_files

def security_node(state):

    report = review_project_files(
        state["generated_project_path"],
        SECURITY_PROMPT
    )

    return complete_stage(
        state=state,
        artifact_name="security_artifact",
        artifact=report,
        next_stage="Testing",
        message="✅ Security completed."
    )
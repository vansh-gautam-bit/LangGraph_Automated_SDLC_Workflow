from app.utils.state_helper import complete_stage

from app.prompts.reviewer import REVIEWER_PROMPT
from app.utils.llm_helper import invoke_llm

def reviewer_node(state):

    prompt = REVIEWER_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="review_artifact",
        artifact=response,
        next_stage="Security",
        message="✅  Review completed."
    )
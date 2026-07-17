from app.utils.state_helper import complete_stage

from app.prompts.reviewer import REVIEWER_PROMPT
from app.utils.llm_helper import invoke_llm

def reviewer_node(state):

    files = state["developer_artifact"]["generated_files"]

    generated_project = "\n\n".join(
        f"### {filename}\n{content}"
        for filename, content in files.items()
    )

    prompt = REVIEWER_PROMPT.format(
        generated_project=generated_project
    )
    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="review_artifact",
        artifact=response,
        next_stage="Security",
        message="✅  Review completed."
    )
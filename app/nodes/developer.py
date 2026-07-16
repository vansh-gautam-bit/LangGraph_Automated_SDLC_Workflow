from app.utils.state_helper import complete_stage

from app.prompts.developer import DEVELOPER_PROMPT
from app.utils.llm_helper import invoke_llm

def developer_node(state):

    prompt = DEVELOPER_PROMPT.format(
        architecture_document=state["architecture_artifact"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="developer_artifact",
        artifact=response,
        next_stage="Reviewer",
        message="✅ Developer completed."
    )
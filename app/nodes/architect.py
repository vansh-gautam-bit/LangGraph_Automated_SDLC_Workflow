from app.utils.state_helper import complete_stage

from app.prompts.architect import ARCHITECT_PROMPT
from app.utils.llm_helper import invoke_llm

def architect_node(state):

    prompt = ARCHITECT_PROMPT.format(
        product_owner_document=state["product_owner_artifact"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="architect_artifact",
        artifact=response,
        next_stage="Developer",
        message="✅ Architecture completed."
    )
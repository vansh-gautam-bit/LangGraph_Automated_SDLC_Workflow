from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage

from app.prompts.product_owner import PRODUCT_OWNER_PROMPT


def product_owner_node(state):

    prompt = PRODUCT_OWNER_PROMPT.format(
        requirements=state["requirements"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="product_owner_artifact",
        artifact=response,
        next_stage="Architect",
        message="✅ Product Owner completed."
    )
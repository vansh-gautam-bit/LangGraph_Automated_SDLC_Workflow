from langchain_core.messages import HumanMessage

from app.prompts.architect import ARCHITECT_PROMPT
from app.utils.llm_helper import invoke_llm

def architect_node(state):

    prompt = ARCHITECT_PROMPT.format(
        product_owner_document=state["product_owner_artifact"]
    )

    response = invoke_llm(prompt)

    state["architecture_artifact"] = response.content

    state["history"].append(
        "✅ Architecture completed."
    )

    state["current_stage"] = "Developer"

    return state
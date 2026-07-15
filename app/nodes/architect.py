from langchain_core.messages import HumanMessage

from app.prompts.architect import ARCHITECT_PROMPT
from app.services.llm import llm

def architect_node(state):

    prompt = ARCHITECT_PROMPT.format(
        product_owner_document=state["product_owner_artifact"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["history"].append(
        "✅ Architecture completed."
    )

    state["current_stage"] = "Developer"

    return state
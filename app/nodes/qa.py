from langchain_core.messages import HumanMessage

from app.prompts.qa import QA_PROMPT
from app.services.llm import llm

def qa_node(state):

    prompt = QA_PROMPT.format(
        review=state["review_artifact"],
        security=state["security_artifact"],
        testing=state["testing_artifact"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["qa_artifact"] = response.content

    state["history"].append(
        "✅ QA completed."
    )

    state["current_stage"] = "Deployment"

    return state
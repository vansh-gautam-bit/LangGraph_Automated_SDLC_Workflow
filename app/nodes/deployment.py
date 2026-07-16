from langchain_core.messages import HumanMessage

from app.prompts.deployment import DEPLOYMENT_PROMPT
from app.services.llm import llm 

def deployment_node(state):

    prompt = DEPLOYMENT_PROMPT.format(
        po=state["product_owner_artifact"],
        architecture=state["architecture_artifact"],
        developer=state["developer_artifact"],
        review=state["review_artifact"],
        security=state["security_artifact"],
        testing=state["testing_artifact"],
        qa=state["qa_artifact"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["deployment_artifact"] = response.content

    state["history"].append(
        "✅ Deployment completed."
    )

    state["current_stage"] = "Completed"

    return state
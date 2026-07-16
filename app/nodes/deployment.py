from app.utils.state_helper import complete_stage

from app.prompts.deployment import DEPLOYMENT_PROMPT
from app.utils.llm_helper import invoke_llm

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

    response = invoke_llm(prompt)

    return complete_stage(
    state=state,
    artifact_name="deployment_artifact",
    artifact=response,
    next_stage="Completed",
    message="✅ Deployment completed."
)
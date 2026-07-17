from app.utils.state_helper import complete_stage

from app.prompts.deployment import DEPLOYMENT_PROMPT
from app.utils.llm_helper import invoke_llm


def deployment_node(state):

    prompt = DEPLOYMENT_PROMPT.format(
        project_path=state["generated_project_path"],
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
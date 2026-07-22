from app.utils.state_helper import complete_stage
from app.prompts.common import OUTPUT_RULES
from app.prompts.deployment import DEPLOYMENT_PROMPT
from app.utils.llm_helper import invoke_llm
from app.utils.human_review import human_review   


def deployment_node(state):

    prompt = DEPLOYMENT_PROMPT.format(
        project_path=state["generated_project_path"],
        qa=state["qa_artifact"],
        previous_artifact=state.get("deployment_artifact", ""),
        feedback=state.get("user_feedback", ""),
        output_rules=OUTPUT_RULES,
    )

    artifact = invoke_llm(prompt)

    human = human_review(
        stage="deployment",
        artifact=artifact,
    )

    state["review_decision"] = human["decision"]
    state["user_feedback"] = human.get("feedback", "")

    return complete_stage(
        state=state,
        artifact_name="deployment_artifact",
        artifact=artifact,
        next_stage="Completed",
        message="✅ Deployment completed."
    )
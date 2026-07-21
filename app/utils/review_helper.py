from langgraph.types import interrupt
from app.utils.llm_helper import invoke_llm

def human_review(
        *,
        stage: str,
        prompt_template: str,
        prompt_variables: dict,
):
    """
    Generic Human-in-the-Loop review helper.

    Returns:
    artifact,
    review_decision,
    user_feedback
    """

    previous_artifact = prompt_variables.get("previous_artifact", "")
    feedback = prompt_variables.get("feedback", "")

    while True:

        prompt = prompt_template.format(
            **prompt_variables,
            previous_artifact=previous_artifact,
            feedback=feedback,
        )

        artifact = invoke_llm(prompt)

        human = interrupt(
            {
                "stage":stage,
                "artifact": artifact,
                "message": f"Review the {stage} artifact and approve or provide feedback."
            }
        )

        if human["decision"] == "approve":

            return (
                artifact,
                "approve",
                ""
            )
        
        previous_artifact= artifact
        feedback = human["feedback"]
        

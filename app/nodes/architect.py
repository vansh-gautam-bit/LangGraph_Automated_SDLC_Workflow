from langchain_core.messages import HumanMessage
from app.utils.state_helper import complete_stage
from app.prompts.architect import ARCHITECT_PROMPT
from app.services.llm import llm
from app.utils.human_review import human_review
from app.utils.llm_helper import invoke_llm

def architect_node(state):

    prompt = ARCHITECT_PROMPT.format(
    product_owner_document=state["product_owner_artifact"],
    previous_artifact=state.get("architecture_artifact", ""),
    feedback=state.get("user_feedback", ""),
)

    artifact = invoke_llm(prompt)

    human = human_review(
    stage="architect",
    artifact=artifact,
    )

    state["review_decision"] = human["decision"]
    state["user_feedback"] = human.get("feedback", "")
   

    return complete_stage(
        state=state,
        artifact_name="architecture_artifact",
        artifact=artifact,
        next_stage="Developer",
        message="✅ Architecture completed."
    )
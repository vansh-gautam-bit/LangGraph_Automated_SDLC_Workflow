from langgraph.types import interrupt

from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage
from app.prompts.product_owner import PRODUCT_OWNER_PROMPT
from app.utils.human_review import human_review
from app.services.memory_service import save_preference, search_preferences

def product_owner_node(state):

    memories = search_preferences(
        state["user_requirements"]
    )

    memory_context = ""

    for memory in memories.get("results", []):
        memory_context += f"- {memory['memory']}\n"

    print("\n===== MEMORIES =====")
    print(memories)
    print("====================\n")

    prompt = PRODUCT_OWNER_PROMPT.format(
        requirements=state["user_requirements"],
        previous_artifact=state.get("product_owner_artifact", ""),
        feedback=state.get("user_feedback", ""),
        memory_context=memory_context,
    )

    artifact = invoke_llm(prompt)

    human = human_review(
    "product_owner",
    artifact=artifact,
    )

    state["review_decision"] = human["decision"]
    state["user_feedback"] = human.get("feedback", "")

    return complete_stage(
        state=state,
        artifact_name="product_owner_artifact",
        artifact=artifact,
        next_stage="Architect",
        message="✅ Product Owner completed."
    )
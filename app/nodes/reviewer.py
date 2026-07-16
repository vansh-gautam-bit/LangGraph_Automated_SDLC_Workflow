from langchain_core.messages import HumanMessage

from app.prompts.reviewer import REVIEWER_PROMPT
from app.services.llm import llm

def reviewer_node(state):

    prompt = REVIEWER_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["review_artifact"] = response.content
    
    state["history"].append(
        "✅ Reviewer completed."
    )

    state["current_stage"] = "Security"

    return state
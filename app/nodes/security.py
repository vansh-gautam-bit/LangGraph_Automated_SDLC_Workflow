from langchain_core.messages import HumanMessage

from app.prompts.security import SECURITY_PROMPT
from app.services.llm import llm

def security_node(state):

    prompt = SECURITY_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["history"].append(
        "✅ Security completed."
    )

    state["current_stage"] = "Testing"

    return state
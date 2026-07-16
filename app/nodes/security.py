from langchain_core.messages import HumanMessage

from app.prompts.security import SECURITY_PROMPT
from app.utils.llm_helper import invoke_llm

def security_node(state):

    prompt = SECURITY_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = invoke_llm(prompt)

    state["security_artifact"] = response.content

    state["history"].append(
        "✅ Security completed."
    )

    state["current_stage"] = "Testing"

    return state
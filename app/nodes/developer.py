from langchain_core.messages import HumanMessage

from app.prompts.developer import DEVELOPER_PROMPT
from app.utils.llm_helper import invoke_llm

def developer_node(state):

    prompt = DEVELOPER_PROMPT.format(
        architecture_document=state["architecture_artifact"]
    )

    response = invoke_llm(prompt)

    state["project_files"]["generated_project.md"] = response.content

    state["developer_artifact"] = response.content

    state["history"].append(
        "✅ Developer completed."
    )

    state["current_stage"] = "Review"

    return state
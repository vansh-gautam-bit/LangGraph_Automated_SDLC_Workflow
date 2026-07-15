from langchain_core.messages import HumanMessage

from app.prompts.developer import DEVELOPER_PROMPT
from app.services.llm import llm

def developer_node(state):

    prompt = DEVELOPER_PROMPT.format(
        architecture_document=state["architecture_artifact"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["project_files"]["generated_project.md"] = response.content

    state["history"].append(
        "✅ Developer completed."
    )

    state["current_stage"] = "Review"

    return state
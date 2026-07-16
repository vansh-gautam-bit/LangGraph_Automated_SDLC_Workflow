from langchain_core.messages import HumanMessage 

from app.prompts.testing import TESTING_PROMPT
from app.services.llm import llm

def testing_node(state):

    prompt = TESTING_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["testing_artifact"] = response.content

    state["history"].append(
        "✅ Testing completed."
    )

    state["current_stage"] = "QA"

    return state
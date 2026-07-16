from app.utils.state_helper import complete_stage

from app.prompts.testing import TESTING_PROMPT
from app.utils.llm_helper import invoke_llm

def testing_node(state):

    prompt = TESTING_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="testing_artifact",
        artifact=response,
        next_stage="QA",
        message="✅ Testing completed."
    )
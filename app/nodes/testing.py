from app.utils.state_helper import complete_stage

from app.prompts.testing import TESTING_PROMPT
from app.utils.llm_helper import invoke_llm

def testing_node(state):

    generated_files = state["developer_artifact"]["generated_files"]

    generated_project = "\n\n".join(
        f"### {filename}\n{content}"
        for filename, content in generated_files.items()
    )

    prompt = TESTING_PROMPT.format(
        generated_project=generated_project
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="testing_artifact",
        artifact=response,
        next_stage="QA",
        message="✅ Testing completed."
    )
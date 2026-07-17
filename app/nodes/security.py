from app.utils.state_helper import complete_stage

from app.prompts.security import SECURITY_PROMPT
from app.utils.llm_helper import invoke_llm


def security_node(state):

    generated_files = state["developer_artifact"]["generated_files"]

    generated_project = "\n\n".join(
        f"### {filename}\n{content}"
        for filename, content in generated_files.items()
    )

    prompt = SECURITY_PROMPT.format(
        generated_project=generated_project
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="security_artifact",
        artifact=response,
        next_stage="Testing",
        message="✅ Security completed."
    )
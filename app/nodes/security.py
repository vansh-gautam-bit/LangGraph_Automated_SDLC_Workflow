from app.utils.state_helper import complete_stage

from app.prompts.security import SECURITY_PROMPT
from app.utils.llm_helper import invoke_llm

def security_node(state):

    prompt = SECURITY_PROMPT.format(
        generated_project=state["project_files"]["generated_project.md"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="security_artifact",
        artifact=response,
        next_stage="Testing",
        message="✅ Security completed."
    )
from app.utils.state_helper import complete_stage

from app.prompts.developer import DEVELOPER_PROMPT
from app.utils.llm_helper import invoke_llm

def developer_node(state):

    prompt = DEVELOPER_PROMPT.format(
        architecture_document=state["architecture_artifact"]
    )

    artifact = invoke_llm(prompt)

    state["project_files"]["generated_project.md"] = artifact

    return complete_stage(
        state=state,
        artifact_name="developer_artifact",
        artifact=artifact,
        next_stage="Reviewer",
        message="✅ Developer completed."
)
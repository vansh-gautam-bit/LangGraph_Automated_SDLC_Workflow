from app.utils.state_helper import complete_stage
from app.subgraphs.developer.graph import developer_graph
from app.prompts.developer import DEVELOPER_PROMPT
from app.utils.llm_helper import invoke_llm

def developer_node(state):

    developer_state = {
        "project_name": state["project_name"],
        "requirements": state["requirements"],

        "product_owner_artifact": state["product_owner_artifact"],
        "architecture_artifact": state["architecture_artifact"],

        "folder_structure": "",

        "models": "",

        "schemas": "",

        "routers": "",
        
        "services": "",

        "generated_files": {},

        "history": [],
    }

    result = developer_graph.invoke(
        developer_state
    )

    return complete_stage(
        state=state,
        artifact_name="developer_artifact",
        artifact=result,
        next_stage="Reviewer",
        message="✅ Developer completed."
    )
from app.utils.state_helper import complete_stage
from app.subgraphs.developer.graph import developer_graph


def developer_node(state):

    developer_state = {
        "project_name": state["project_name"],
        "user_requirements": state["user_requirements"],
        "product_owner_artifact": state["product_owner_artifact"],
        "architecture_artifact": state["architecture_artifact"],
        "folder_structure": "",
        "models": "",
        "schemas": "",
        "routers": "",
        "services": "",
        "readme": "",
        "generated_files": {},
        "history": [],
        "user_feedback": state.get("user_feedback", "",)
    }

    result = developer_graph.invoke(developer_state)

    developer_artifact = {
    "folder_structure": result["folder_structure"], 
    "generated_files": result["generated_files"],
    }

    return complete_stage(
        state=state,
        artifact_name="developer_artifact",
        artifact=developer_artifact,
        next_stage="Reviewer",
        message="✅ Developer completed."
    )
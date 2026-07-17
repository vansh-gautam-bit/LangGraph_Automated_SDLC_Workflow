from pathlib import Path

def writer_node(state):

    project_name = state["project_name"]

    generated_files = state["developer_artifact"]["generated_files"]

    root = Path("generated_projects") / project_name

    root.mkdir(parents=True, exist_ok=True)

    for filename, content in generated_files.items():

        file_path = root / filename

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(content, encoding="utf-8")

    state["generated_project_path"] = str(root)

    state["writer_status"] = "Project written successfully."

    state["history"].append("Project file created.")

    return state    

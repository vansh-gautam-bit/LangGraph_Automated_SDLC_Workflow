from app.prompts.folder_generator import FOLDER_GENERATOR_PROMPT

from app.utils.llm_helper import invoke_llm

def folder_generator_node(state):

    prompt = FOLDER_GENERATOR_PROMPT.format(
    project_name=state["project_name"],
    architecture=state["architecture_artifact"],
)

    folder_structure = invoke_llm(prompt)

    state["folder_structure"] = folder_structure
    
    state["history"].append(
        "Folder structure generated."
    )
    
    return state
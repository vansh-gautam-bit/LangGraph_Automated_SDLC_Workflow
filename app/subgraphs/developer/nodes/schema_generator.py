from app.prompts.schema_generator import SCHEMA_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm

def schema_generator_node(state):

    prompt = SCHEMA_GENERATOR_PROMPT.format(
        project_name=state["project_name"],
        requirements=state["user_requirements"],
        product_owner= state["product_owner_artifact"],
        architecture=["architecture_artifact"],
        folder_structure=state["folder_structure"],
        models=state["models"]
    )

    schemas = invoke_llm(prompt)

    state["schemas"] = schemas
    state["generated_files"]["schemas.py"] = schemas

    state["history"].append(
        "Schemas generated."
    )

    return state
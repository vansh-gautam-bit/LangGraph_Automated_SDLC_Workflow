from app.prompts.model_generator import MODEL_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm

def model_generator_node(state):

    prompt = MODEL_GENERATOR_PROMPT.format(
        project_name=state["project_name"],
        requirements=state["requirements_artifact"],
        product_owner=state["product_owner_artifact"],
        architecture=state["architecture_artifact"],
        folder_structure=state["folder_structure"],
    )

    models = invoke_llm(prompt)

    state["models"] = models
    state["generated_files"]["models.py"] = models

    state["history"].append(
        "Models generated."
    )

    return state
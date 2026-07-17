from app.prompts.service_generator import SERVICE_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm

def service_generator_node(state):

    prompt = SERVICE_GENERATOR_PROMPT.format(
        project_name=state["project_name"],
        requirements=state["user_requirements"],
        product_owner=state["product_owner_artifact"],
        architecture=state["architecture_artifact"],
        folder_structure=state["folder_structure"],
        models=state["models"],
        schemas=state["schemas"],
        routers=state["routers"],
    )

    services = invoke_llm(prompt)

    state["services"] = services
    state["generated_files"]["services.py"] = services

    state["history"].append(
        "Service generated."
    )

    return state
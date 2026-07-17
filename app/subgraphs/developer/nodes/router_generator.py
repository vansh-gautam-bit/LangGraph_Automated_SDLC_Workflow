from app.prompts.router_generator import ROUTER_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm

def router_generator_node(state):

    prompt = ROUTER_GENERATOR_PROMPT.format(
        project_name=state["project_name"],
        requirements=state["user_requirements"],
        product_owner=state["product_owner_artifact"],
        architecture=state["architecture_artifact"],
        folder_structure=state["folder_structure"],
        models=state["models"],
        schemas=state["schemas"],
    )

    routers = invoke_llm(prompt)

    state["routers"] = routers
    state["generated_files"]["routers.py"] = routers

    state["history"].append(
        "Routers generated."
    )
    return state
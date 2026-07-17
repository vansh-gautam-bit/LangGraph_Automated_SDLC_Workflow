from app.prompts.router_generator import ROUTER_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm

def router_generator_node(state):

    prompt = ROUTER_GENERATOR_PROMPT.format(
    requirements=state["user_requirements"],
    schemas=state["schemas"],
    services=state["services"],
)

    routers = invoke_llm(prompt)

    state["routers"] = routers
    state["generated_files"]["routers.py"] = routers

    state["history"].append(
        "Routers generated."
    )
    return state
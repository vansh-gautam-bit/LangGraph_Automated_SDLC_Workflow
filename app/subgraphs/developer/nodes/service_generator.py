from app.prompts.service_generator import SERVICE_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm


def service_generator_node(state):

    prompt = SERVICE_GENERATOR_PROMPT.format(
        requirements=state["user_requirements"],
        models=state["models"],
        schemas=state["schemas"],
    )

    services = invoke_llm(prompt)

    state["services"] = services
    state["generated_files"]["app/services.py"] = services

    state["history"].append("Services generated.")

    return state
from app.prompts.readme_generator import README_GENERATOR_PROMPT
from app.utils.llm_helper import invoke_llm
from app.prompts.common import OUTPUT_RULES

def readme_generator_node(state):

    prompt = README_GENERATOR_PROMPT.format(
        project_name=state["project_name"],
        requirements=state["user_requirements"],
        product_owner=state["product_owner_artifact"],
        architecture=state["architecture_artifact"],
        folder_structure=state["folder_structure"],
        models=state["models"],
        schemas=state["schemas"],
        routers=state["routers"],
        services=state["services"],
        output_rules=OUTPUT_RULES,
    )    

    readme = invoke_llm(prompt)

    state["readme"] = readme
    state["generated_files"]["README.md"] = readme

    state["history"].append(
        "README generated."
    )
    
    return state
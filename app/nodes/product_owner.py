# from app.services.llm import llm
# from app.state import SDLCState
# from app.prompts.product_owner import PRODUCT_OWNER_PROMPT
# from app.schemas.artifacts import ProductOwnerArtifact

# def product_owner_nodes(state: SDLCState):

#     prompt = PRODUCT_OWNER_PROMPT.format(
#         requirements=state["requirements"]
#     )

#     structured_llm = llm.with_structured_output(
#         ProductOwnerArtifact
#     )

#     artifact = structured_llm.invoke(prompt)

#     artifact.stage = "Product Owner"
#     artifact.status = "completed"

#     state["product_owner_artifact"] = artifact

#     state["history"].append(
#         "Product Owner completed."
#     )

#     state["current_stage"] = "Architecture"

#     return state


from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage

from app.prompts.product_owner import PRODUCT_OWNER_PROMPT


def product_owner_node(state):

    prompt = PRODUCT_OWNER_PROMPT.format(
        requirements=state["requirements"]
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="product_owner_artifact",
        artifact=response,
        next_stage="Architecture",
        message="✅ Product Owner completed."
    )
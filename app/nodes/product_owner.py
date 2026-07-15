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


from langchain_core.messages import HumanMessage

from app.prompts.product_owner import PRODUCT_OWNER_PROMPT
from app.services.llm import llm


def product_owner_node(state):

    prompt = PRODUCT_OWNER_PROMPT.format(
        requirements=state["requirements"]
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    state["product_owner_artifact"] = response.content

    state["history"].append(
        "✅ Product Owner completed."
    )

    state["current_stage"] = "Architecture"

    return state
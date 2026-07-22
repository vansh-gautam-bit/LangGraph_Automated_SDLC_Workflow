from app.utils.state_helper import complete_stage
from app.prompts.common import OUTPUT_RULES
from app.prompts.qa import QA_PROMPT
from app.utils.llm_helper import invoke_llm

def qa_node(state):

    prompt = QA_PROMPT.format(
        review=state["review_artifact"],
        security=state["security_artifact"],
        testing=state["testing_artifact"],
        output_rules=OUTPUT_RULES,
    )

    response = invoke_llm(prompt)

    return complete_stage(
        state=state,
        artifact_name="qa_artifact",
        artifact=response,
        next_stage="Deployment",
        message="✅ QA completed."
    )
from langchain_core.messages import HumanMessage
from app.services.llm import llm

def invoke_llm(prompt: str) -> str:
    """
    Invoke the configured LLM
    and return plain text.
    """

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content
import time

from langchain_core.messages import HumanMessage
from app.services.llm import llm


def invoke_llm(prompt: str) -> str:
    """
    Invoke the configured LLM with retries.
    """

    last_exception = None

    for attempt in range(3):
        try:
            response = llm.invoke(
                [HumanMessage(content=prompt)]
            )

            return response.content

        except Exception as e:
            last_exception = e

            print(f"LLM attempt {attempt + 1} failed: {e}")

            if attempt < 2:
                time.sleep(2 ** attempt)  # 1 sec, then 2 sec

    raise last_exception
from app.memory import memory

USER_ID = "default_user"

def save_preference(text: str):
    """
    Save a user preferance to Mem0.
    """
    memory.add(
        messages=text,
        user_id=USER_ID,
    )

def search_preferences(query: str):
    """
    Retrieve relevant memories.
    """

    return memory.search(
        query=query,
        filters={
            "user_id": USER_ID
        }
    )
from app.state import SDLCState


def complete_stage(
    state: SDLCState,
    artifact_name: str,
    artifact: str,
    next_stage: str,
    message: str,
) -> SDLCState:

    state[artifact_name] = artifact
    state["history"].append(message)
    state["current_stage"] = next_stage

    return state
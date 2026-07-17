from pathlib import Path

from app.prompts.testing import TESTING_PROMPT
from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage


def testing_node(state):

    project_path = Path(state["generated_project_path"])

    files_to_test = [
        "app/models.py",
        "app/schemas.py",
        "app/services.py",
        "app/routers.py",
    ]

    reports = []

    for file in files_to_test:

        file_path = project_path / file

        if not file_path.exists():
            continue

        code = file_path.read_text(encoding="utf-8")

        prompt = TESTING_PROMPT.format(
            filename=file,
            code=code,
        )

        response = invoke_llm(prompt)

        reports.append(
            f"# {file}\n\n{response}"
        )

    final_report = "\n\n".join(reports)

    return complete_stage(
        state=state,
        artifact_name="testing_artifact",
        artifact=final_report,
        next_stage="QA",
        message="✅ Testing completed."
    )
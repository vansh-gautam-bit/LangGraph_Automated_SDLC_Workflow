from pathlib import Path

from app.prompts.reviewer import REVIEWER_PROMPT
from app.utils.llm_helper import invoke_llm
from app.utils.state_helper import complete_stage


def reviewer_node(state):

    project_path = Path(state["generated_project_path"])

    files_to_review = [
        "app/models.py",
        "app/schemas.py",
        "app/services.py",
        "app/routers.py",
        "README.md",
    ]

    reports = []

    for file in files_to_review:

        file_path = project_path / file

        if not file_path.exists():
            continue

        code = file_path.read_text(encoding="utf-8")

        prompt = REVIEWER_PROMPT.format(
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
        artifact_name="review_artifact",
        artifact=final_report,
        next_stage="Security",
        message="✅ Review completed."
    )
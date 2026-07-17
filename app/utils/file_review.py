from pathlib import Path

from app.constants import CODE_FILES
from app.utils.llm_helper import invoke_llm

def review_project_files(project_path, prompt_template):

    reports = []

    project_path = Path(project_path)

    for file in CODE_FILES:

        path = project_path / file

        if not path.exists():
            continue

        code = path.read_text(encoding="utf-8")

        prompt = prompt_template.format(
            filename=file,
            code=code,
        )

        response = invoke_llm(prompt)

        reports.append(f"# {file}\n\n{response}")

    return "\n\n".join(reports)
from typing import TypedDict

from app.schemas.artifacts import (
    ArchitectureArtifact,
    DeploymentArtifact,
    DeveloperArtifact,
    ProductOwnerArtifact,
    QAArtifact,
    ReviewArtifact,
    SecurityArtifact,
    TestingArtifact,
)

class SDLCState(TypedDict):
    generated_project_path: str

    writer_status: str

    project_name: str

    user_requirements: str

    project_files: dict[str, str]

    product_owner_artifact: str |None

    architecture_artifact: str| None

    developer_artifact: str |None

    review_artifact: str|None

    security_artifact: str| None

    testing_artifact: str |None

    qa_artifact : str | None

    deployment_artifact: str |None

    review_descision: str | None

    user_feedback: str | None

    current_stage: str

    history: list[str]
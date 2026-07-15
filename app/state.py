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
    project_name: str

    requirements: str

    project_files: dict[str, str]

    product_owner_artifact: str |None

    architecture_artifact: str| None

    developer_artifact: str |None

    review_artifact: str|None

    security_artifact: str| None

    testing_artifact: str |None

    qa_artifact : str | None

    deployment_artifact: str |None

    current_stage: str

    history: list[str]
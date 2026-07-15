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

    product_owner_artifacts: ProductOwnerArtifact |None

    architecture_artifact: ArchitectureArtifact| None

    developer_artifact: DeveloperArtifact |None

    review_artifact: ReviewArtifact |None

    security_artifact: SecurityArtifact | None

    testing_artifact: TestingArtifact |None

    qa_artifact : QAArtifact | None

    deployment_artifact: DeploymentArtifact |None

    current_stage: str

    history: list[str]
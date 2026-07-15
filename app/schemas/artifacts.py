from typing import Literal

from pydantic import BaseModel, Field

class BaseArtifact(BaseModel):
    stage: str
    status: Literal["completed","rejected","revision_required"]
    summary: str
    recommendation: str
    confidence: float = Field(..., ge=0.0, le=1.0)

class ProductOwnerArtifact(BaseArtifact):
    project_vision: str
    user_stories: list[str]
    acceptance_criteria: list[str]
    risks: list[str]

class ArchitectureArtifact(BaseArtifact):
    architecture_summary: str
    folder_structure: str
    database_design: str
    api_design: str

class DeveloperArtifact(BaseArtifact):
    generated_files: list[str]
    modified_files: list[str]

class ReviewArtifact(BaseArtifact):
    score: float =Field(..., ge=0.0, le=10.0)
    issues: list[str]

class SecurityArtifact(BaseArtifact):
    critical: list[str]
    high: list[str]
    low: list[str]

class TestingArtifact(BaseArtifact):
    generated_tests: list[str]
    coverage: float = Field(..., ge=0.0, le=100.0)    

class QAArtifact(BaseArtifact):
    passed: bool
    failed_cases: list[str]

class DeploymentArtifact(BaseArtifact):
    deployment_steps: list[str]
    docker_ready: bool                    


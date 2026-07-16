from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, Field

class BaseArtifact(BaseModel):
    artifact_id: str = Field(default_facfactory=lambda: str(uuid4()))
    stage: str = ""
    status: Literal["completed","rejected","revision_required"] = "completed"
    executive_summary: str
    recommendation: str
    confidence: float = Field(..., ge=0.0, le=1.0)

class ProductOwnerArtifact(BaseArtifact):
    project_vision: str
    functional_requirements: list[str]
    user_stories: list[str]
    acceptance_criteria: list[str]
    assumptions: list[str]
    risks: list[str]

class ArchitectureArtifact(BaseArtifact):
    architecture_summary: str
    folder_structure: list[str]
    database_design: str
    api_design: list[str]

class DeveloperArtifact(BaseArtifact):
    generated_files: dict[str, str]
    modified_files: dict[str, str]

class ReviewArtifact(BaseArtifact):
    score: float =Field(..., ge=0.0, le=10.0)
    issues: list[str]

class SecurityArtifact(BaseArtifact):
    critical: list[str]
    high: list[str]
    medium: list[str]
    low: list[str]

class TestingArtifact(BaseArtifact):
    generated_tests: dict[str, str]
    coverage: float = Field(..., ge=0.0, le=100.0)    

class QAArtifact(BaseArtifact):
    passed: bool
    failed_cases: list[str]

class DeploymentArtifact(BaseArtifact):
    deployment_steps: list[str]
    docker_ready: bool                    


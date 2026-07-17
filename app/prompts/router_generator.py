ROUTER_GENERATOR_PROMPT = """
You are a Senior FastAPI Backend Engineer.

Generate a production-ready `routers.py` file.

## Project Name
{project_name}

## User Requirements
{requirements}

## Product Owner Specification
{product_owner}

## Architecture Specification
{architecture}

## Folder Structure
{folder_structure}

## SQLAlchemy Models
{models}

## Pydantic Schemas
{schemas}

## Instructions

Generate FastAPI CRUD routes.

Requirements:

- Use APIRouter.
- Follow REST conventions.
- Include GET, POST, PUT, DELETE endpoints.
- Use dependency injection.
- Use proper response models.
- Call service layer only.
- Do NOT write business logic.
- Include imports.
- Use async endpoints.
- Use proper HTTP status codes.

Return ONLY Python code.
"""
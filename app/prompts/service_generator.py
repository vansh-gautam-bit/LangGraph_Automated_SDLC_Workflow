SERVICE_GENERATOR_PROMPT = """
You are a Senior Python Backend Engineer.

Generate a production-ready `services.py` file.

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

## Router Code
{routers}

## Instructions

Generate the service layer.

Requirements:

- Implement CRUD operations.
- Use SQLAlchemy ORM.
- Keep business logic here.
- No FastAPI routes.
- No Pydantic models.
- Use dependency injection where appropriate.
- Handle exceptions gracefully.
- Add type hints.
- Follow clean architecture.
- Import everything needed.

Return ONLY Python code.
"""
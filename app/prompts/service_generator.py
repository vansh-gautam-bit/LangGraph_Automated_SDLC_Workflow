SERVICE_GENERATOR_PROMPT = """
You are a Senior Python Backend Engineer.

Generate a production-ready `services.py` file.

## User Requirements
{requirements}

## SQLAlchemy Models
{models}

## Pydantic Schemas
{schemas}

## Instructions

Generate only the service layer.

Requirements:

- Implement complete CRUD operations.
- Use SQLAlchemy ORM.
- Place all business logic inside the service layer.
- Do NOT generate FastAPI routes.
- Do NOT generate Pydantic schemas.
- Use the provided models and schemas.
- Add proper type hints.
- Handle exceptions gracefully.
- Follow clean architecture principles.
- Include all necessary imports.

Return ONLY valid Python code.
"""
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
- Use dependency injection where appropriate.
- Use SQLAlchemy sessions correctly.
- Keep business logic inside the service layer.

OUTPUT RULES:

- Return ONLY valid Python code.
- No Markdown.
- No ``` blocks.
- No explanations.
- Output must be directly writable into services.py.
"""
MODEL_GENERATOR_PROMPT = """
You are a Senior Python Backend Engineer.

Generate a production-ready SQLAlchemy `models.py` file.

## User Requirements
{requirements}

## Architecture
{architecture}

## Instructions

Generate SQLAlchemy ORM models based on the requirements and architecture.

Requirements:

- Use SQLAlchemy ORM.
- Include relationships where appropriate.
- Use proper type annotations.
- Define primary keys and foreign keys correctly.
- Use meaningful table names.
- Include all necessary imports.
- Follow clean architecture principles.
- Return ONLY valid Python code.
"""
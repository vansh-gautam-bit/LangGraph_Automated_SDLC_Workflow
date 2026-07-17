ROUTER_GENERATOR_PROMPT = """
You are a Senior FastAPI Backend Engineer.

Generate a production-ready `routers.py` file.

## User Requirements
{requirements}

## Pydantic Schemas
{schemas}

## Service Layer
{services}

## Instructions

Generate FastAPI CRUD routes.

Requirements:

- Use APIRouter.
- Follow RESTful conventions.
- Include GET, POST, PUT and DELETE endpoints.
- Use dependency injection.
- Use the provided Pydantic schemas as request and response models.
- Call ONLY the service layer.
- Do NOT write business logic.
- Do NOT access SQLAlchemy models directly.
- Include all required imports.
- Use async endpoints where appropriate.
- Return proper HTTP status codes.

Return ONLY valid Python code.
"""
FOLDER_GENERATOR_PROMPT = """
You are a Senior Software Architect.

Generate the folder structure for a FastAPI backend project.

## Project Name
{project_name}

## Architecture
{architecture}

## Instructions

Generate a clean and scalable folder structure.

Requirements:

- Follow FastAPI best practices.
- Separate routers, services, models and schemas.
- Include config, database and utils folders where appropriate.
- Return ONLY the folder tree.
"""
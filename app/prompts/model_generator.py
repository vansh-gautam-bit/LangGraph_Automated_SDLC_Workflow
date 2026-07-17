MODEL_GENERATOR_PROMPT = """
You are a Senior Python Backend Engineer.

Your task is to generate SQLAlchemy OMR models for the project.

Project Name:
{project_name}

User Requirements:
{requirements}

Product Owner Analysis:
{product_owner}

Architecture Design:
{architecture}

Folder Structure:
{folder_structure}

Instructions:
- Generate clean SQLAlchemy models.
- use relationships were appropriate.
- Use type annotations.
- Return ONLY Python code.

"""
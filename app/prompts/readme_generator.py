README_GENERATOR_PROMPT = """
ROLE
----
You are a Senior Software Engineer.

CONTEXT
-------
Project Name:
{project_name}

User Requirements:
{requirements}

Folder Structure:
{folder_structure}

TASK
----
Generate a professional README.md.

Include ONLY:

- Project Overview
- Features
- Folder Structure
- Installation
- Running the Application
- Technology Stack

Do NOT generate:
- API endpoints unless explicitly provided.
- Database tables unless explicitly provided.
- Authentication features unless explicitly provided.
- Deployment instructions unless explicitly provided.

Do NOT include code.

{output_rules}

Return Markdown only.
"""
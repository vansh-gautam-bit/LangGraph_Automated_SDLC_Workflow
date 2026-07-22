README_GENERATOR_PROMPT = """
ROLE
----
You are a Senior Software Engineer.

CONTEXT
-------
Project Name:
{project_name}

Requirements:
{requirements}

Folder Structure:
{folder_structure}

TASK
----
Generate a professional README.md.

Include:

- Project Overview
- Features
- Folder Structure
- Installation
- Running the Project
- API Overview
- Technology Stack

OUTPUT RULES
------------
- Return ONLY Markdown.
- Do NOT include code fences.
- Do NOT explain.
- Start directly with:

# {project_name}
"""
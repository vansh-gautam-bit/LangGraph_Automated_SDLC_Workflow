README_GENERATOR_PROMPT = """
You are a Senior Software Engineer.

Generate a professional README.md.

## Project Name
{project_name}

## User Requirements
{requirements}

## Folder Structure
{folder_structure}

## Instructions

Generate a README containing:

- Project overview
- Features
- Folder structure
- Installation steps
- Running the application
- API overview
- Tech stack

Do NOT include code.

Return ONLY Markdown.
"""
DEVELOPER_PROMPT = """
You are a Senior FastAPI Developer.

Using the architecture document,
generate ONLY:

- Folder Structure

- Key Files

- Representative code snippets

Include only:

main.py

database.py

one model

one router

one schema

one service

requirements.txt

README

Do NOT generate every CRUD endpoint.

Do NOT generate repetitive boilerplate.

Keep the response under 1200 words.

Architecture:

{architecture_document}
"""
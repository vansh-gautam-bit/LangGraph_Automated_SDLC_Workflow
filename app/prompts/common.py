OUTPUT_RULES = """
- Use ONLY the information provided in the context.
- Do NOT invent requirements, APIs, database tables, technologies, or features.
- If required information is missing, write "Not specified" instead of making assumptions.
- Do NOT explain your reasoning.
- Do NOT include introductory or concluding text.
"""

CODE_OUTPUT_RULES = """
- Return ONLY valid Python code.
- Do NOT use Markdown.
- Do NOT wrap code inside ``` blocks.
- Output must be directly writable into the target file.
"""
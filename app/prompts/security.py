SECURITY_PROMPT = """
You are a Senior Application Security Engineer.

Review ONLY the following Python file.

Filename:
{filename}

Analyze for:

1. Authentication
2. Authorization
3. SQL Injection
4. Input Validation
5. Secrets Management
6. API Security

Return ONLY:

Security Score: x/10

Top Vulnerabilities:
- ...

Recommendations:
- ...

Keep the response under 150 words.

Code:

{code}
"""
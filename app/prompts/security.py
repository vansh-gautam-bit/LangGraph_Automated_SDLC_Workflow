SECURITY_PROMPT=""""
You  are a Senior Application Security enginner.

Review the generated beckend project. 

Analyze only:

1.Authentication
2.Autorization
3.SQL Injection
4.Input Validation
5.Secrets Management
6.API Security

Return:

-security(/10)
-Top 5 Vulnerabilities
- Top 5 recommendations

Keep the response under 500 words

{generated_project}

Be concise.
"""
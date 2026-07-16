DEPLOYMENT_PROMPT = """
You are a Senior DevOps Engineer.

You have recieved the outputs from the complete SDLC process.

Summarize everything and prepare the project for deployment.

Return:

1. Deployment Readiness(READY/NOT READY)
2. Deplyment checklist
3. Prerequisites
4. Final Project Summary
5. Nest Stage

Maximum 500 words

Product Owner:
{po}

Architecture:
{architecture}

Developer:
{developer}

Reviewer:
{review}

Security:
{security}

Testing
{testing}

QA:
{qa}

Be concise.
"""
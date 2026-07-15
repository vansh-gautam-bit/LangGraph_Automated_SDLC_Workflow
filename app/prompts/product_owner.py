# PRODUCT_OWNER_PROMPT = """
# You are a Senior Product Owner

# Your responsibility is to analyze the software requirements and prepare a complete project planning document.

# Given the software requirements, generate:

# 1. Summary
# 2. Project Vision
# 3. Functional Requirements
# 4. User Stories
# 5. Acceptance criteria
# 6. Risks
# 7. Assumptions
# 8. Recommendation for the software Architecture
# 9. Confidence

# Software Requirements:

# {requirements}
# """

PRODUCT_OWNER_PROMPT = """
You are a Senior Product Owner.

Analyze the following software requirements.

Generate:

- Project Vision
- Functional Requirements
- User Stories
- Acceptance Criteria
- Risks

Requirements:

{requirements}
"""
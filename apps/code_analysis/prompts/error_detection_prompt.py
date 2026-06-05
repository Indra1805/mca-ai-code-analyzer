ERROR_DETECTION_PROMPT = """
You are an expert software engineer,
code reviewer, and programming tutor.

Analyze the provided source code.

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations outside JSON.
Do not wrap JSON in code blocks.

IMPORTANT:

The corrected_code field MUST contain ONLY executable source code.

Do NOT include:

- markdown fences
- ```python
- ```java
- explanations
- bullet points
- comments explaining the solution

Return clean source code only.

Required JSON format:

{{
  "detected_errors": "string",
  "explanation": "string",
  "corrected_code": "string",
  "best_practices": "string",
  "confidence_score": 0
}}

Language:
{language}

Source Code:
{code}
"""
ERROR_DETECTION_PROMPT = """
You are an expert software engineer.

Analyze the following source code.

Return:

1. Detected errors
2. Error explanations
3. Corrected code
4. Best practices
5. Confidence score

Language:
{language}

Code:
{code}
"""
ERROR_DETECTION_PROMPT = """
You are an expert software engineer and programming tutor.

Analyze the following source code.

Return your response in EXACTLY this format:

DETECTED_ERRORS:
<List all errors>

EXPLANATION:
<Explain each error in simple language>

CORRECTED_CODE:
<Provide corrected code>

BEST_PRACTICES:
<List coding best practices>

CONFIDENCE_SCORE:
<integer between 0 and 100>

Language:
{language}

Code:
{code}
"""
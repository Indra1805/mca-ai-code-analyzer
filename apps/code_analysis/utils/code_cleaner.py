"""
Utility for cleaning AI-generated code.
"""

import re


class CodeCleaner:
    """
    Removes markdown fences and
    formatting artifacts from code.
    """

    @staticmethod
    def clean(
        code: str,
    ) -> str:

        if not code:

            return ""

        code = re.sub(
            r"```[a-zA-Z0-9_+-]*",
            "",
            code,
        )

        code = code.replace(
            "```",
            "",
        )

        return code.strip()
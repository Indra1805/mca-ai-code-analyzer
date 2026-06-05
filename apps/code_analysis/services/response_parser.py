"""
Parse Gemini responses into structured fields.
"""

import re

from apps.code_analysis.dto.analysis_result import (
    AnalysisResult,
)


class ResponseParser:

    @staticmethod
    def parse(
        response_text: str,
        language: str,
    ) -> AnalysisResult:

        def extract(section):

            pattern = (
                rf"{section}:\s*(.*?)(?=\n[A-Z_]+:|$)"
            )

            match = re.search(
                pattern,
                response_text,
                re.DOTALL,
            )

            return (
                match.group(1).strip()
                if match
                else ""
            )

        confidence = extract(
            "CONFIDENCE_SCORE"
        )

        try:

            confidence = int(
                re.findall(
                    r"\d+",
                    confidence,
                )[0]
            )

        except Exception:

            confidence = 0

        return AnalysisResult(
            language=language,
            detected_errors=extract(
                "DETECTED_ERRORS"
            ),
            explanation=extract(
                "EXPLANATION"
            ),
            corrected_code=extract(
                "CORRECTED_CODE"
            ),
            best_practices=extract(
                "BEST_PRACTICES"
            ),
            confidence_score=confidence,
        )
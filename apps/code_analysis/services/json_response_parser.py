"""
JSON response parser.
"""

import json

from apps.code_analysis.dto.analysis_result import (
    AnalysisResult,
)


class JSONResponseParser:

    @staticmethod
    def parse(
        response_text,
        language,
    ):

        try:

            data = json.loads(
                response_text
            )

            return AnalysisResult(
                language=language,
                detected_errors=data.get(
                    "detected_errors",
                    "",
                ),
                explanation=data.get(
                    "explanation",
                    "",
                ),
                corrected_code=data.get(
                    "corrected_code",
                    "",
                ),
                best_practices=data.get(
                    "best_practices",
                    "",
                ),
                confidence_score=int(
                    data.get(
                        "confidence_score",
                        0,
                    )
                ),
            )

        except Exception:

            raise ValueError(
                "Invalid Gemini JSON response."
            )
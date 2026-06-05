"""
Code analysis service.
"""

from apps.code_analysis.dto.analysis_result import (
    AnalysisResult,
)

from apps.code_analysis.prompts.error_detection_prompt import (
    ERROR_DETECTION_PROMPT,
)

from apps.code_analysis.repositories.analysis_repository import (
    AnalysisRepository,
)

from apps.code_analysis.services.gemini_service import (
    GeminiService,
)

from apps.code_analysis.validators.code_validator import (
    CodeValidator,
)


class AnalysisService:

    def __init__(self):

        self.gemini_service = (
            GeminiService()
        )

    def analyze_code(
        self,
        *,
        user,
        language,
        code,
    ):

        CodeValidator.validate(
            code
        )

        prompt = (
            ERROR_DETECTION_PROMPT
            .format(
                language=language,
                code=code,
            )
        )

        response_text = (
            self.gemini_service
            .generate_content(
                prompt
            )
        )

        from apps.code_analysis.services.response_parser import (
            ResponseParser
        )

        result = ResponseParser.parse(
            response_text,
            language,
        )

        AnalysisRepository.create_analysis(
            user=user,
            language=language,
            source_code=code,
            detected_errors=result.detected_errors,
            explanation=result.explanation,
            corrected_code=result.corrected_code,
            best_practices=result.best_practices,
            confidence_score=result.confidence_score,
        )

        return result
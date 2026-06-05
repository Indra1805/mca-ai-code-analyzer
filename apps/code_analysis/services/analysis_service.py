"""
Code analysis service.
"""

import logging
import time

from apps.code_analysis.models import (
    AnalysisHistory,
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

from apps.code_analysis.services.json_response_parser import (
    JSONResponseParser,
)

from apps.code_analysis.utils.json_cleaner import (
    JSONCleaner,
)

from apps.code_analysis.validators.code_validator import (
    CodeValidator,
)

from apps.code_analysis.utils.code_cleaner import (
    CodeCleaner,
)

logger = logging.getLogger(__name__)


class AnalysisService:
    """
    Handles code analysis workflow.
    """

    def __init__(self):

        self.gemini_service = GeminiService()

    def analyze_code(
        self,
        *,
        user,
        language,
        code,
    ):
        """
        Analyze source code using Gemini.
        """

        try:

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

            start_time = time.time()

            response_text = (
                self.gemini_service
                .generate_content(
                    prompt
                )
            )

            end_time = time.time()

            duration_ms = int(
                (end_time - start_time)
                * 1000
            )

            cleaned_response = (
                JSONCleaner.clean(
                    response_text
                )
            )

            result = (
                JSONResponseParser
                .parse(
                    cleaned_response,
                    language,
                )
            )

            result.corrected_code = (
                CodeCleaner.clean(
                    result.corrected_code
                )
            )

            analysis_record = (
                AnalysisRepository
                .create_analysis(
                    user=user,
                    language=language,
                    source_code=code,
                    detected_errors=result.detected_errors,
                    explanation=result.explanation,
                    corrected_code=result.corrected_code,
                    best_practices=result.best_practices,
                    raw_response=response_text,
                    confidence_score=result.confidence_score,
                    analysis_duration_ms=duration_ms,
                    analysis_status=(
                        AnalysisHistory
                        .AnalysisStatus
                        .SUCCESS
                    ),
                )
            )

            return {
                "result": result,
                "analysis": analysis_record,
            }

        except Exception as exc:

            logger.exception(
                f"Analysis failed: {exc}"
            )

            AnalysisRepository.create_analysis(
                user=user,
                language=language,
                source_code=code,
                raw_response=str(exc),
                analysis_status=(
                    AnalysisHistory
                    .AnalysisStatus
                    .FAILED
                ),
            )

            raise
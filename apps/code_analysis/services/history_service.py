from apps.code_analysis.repositories.analysis_repository import (
    AnalysisRepository,
)


class HistoryService:

    @staticmethod
    def get_filtered_history(
        *,
        user,
        query=None,
        language=None,
    ):

        return (
            AnalysisRepository
            .search_analyses(
                user=user,
                query=query,
                language=language,
            )
        )
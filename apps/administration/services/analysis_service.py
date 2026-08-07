from apps.administration.repositories.analysis_repository import (
    AnalysisRepository,
)


class AnalysisService:

    @staticmethod
    def get_analyses(
        search="",
        language="",
        status="",
    ):

        return AnalysisRepository.get_analyses(
            search=search,
            language=language,
            status=status,
        )

    @staticmethod
    def get_analysis(pk):

        return AnalysisRepository.get_analysis(pk)

    @staticmethod
    def delete_analysis(pk):

        AnalysisRepository.delete_analysis(pk)
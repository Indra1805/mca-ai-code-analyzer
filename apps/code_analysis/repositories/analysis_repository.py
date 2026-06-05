from django.db.models import Q

from apps.code_analysis.models import (
    AnalysisHistory,
)


class AnalysisRepository:

    @staticmethod
    def create_analysis(**kwargs):
        return AnalysisHistory.objects.create(
            **kwargs
        )

    @staticmethod
    def get_analysis_by_id(pk):
        return (
            AnalysisHistory.objects
            .filter(id=pk)
            .first()
        )

    @staticmethod
    def get_user_analyses(user):

        return (
            AnalysisHistory.objects
            .filter(user=user)
            .order_by("-created_at")
        )

    @staticmethod
    def search_analyses(
        *,
        user,
        query=None,
        language=None,
    ):

        analyses = (
            AnalysisHistory.objects
            .filter(user=user)
        )

        if query:

            analyses = analyses.filter(
                Q(language__icontains=query)
                |
                Q(source_code__icontains=query)
            )

        if language:

            analyses = analyses.filter(
                language=language
            )

        return analyses.order_by(
            "-created_at"
        )
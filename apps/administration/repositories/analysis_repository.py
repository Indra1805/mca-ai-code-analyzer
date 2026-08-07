from django.db.models import Q

from apps.code_analysis.models import AnalysisHistory


class AnalysisRepository:

    @staticmethod
    def get_analyses(
        search="",
        language="",
        status="",
    ):

        queryset = (
            AnalysisHistory.objects
            .select_related("user")
            .order_by("-created_at")
        )

        if search:

            queryset = queryset.filter(
                Q(user__username__icontains=search)
                |
                Q(language__icontains=search)
            )

        if language:

            queryset = queryset.filter(
                language=language
            )

        if status:

            queryset = queryset.filter(
                analysis_status=status
            )

        return queryset

    @staticmethod
    def get_analysis(pk):

        return (
            AnalysisHistory.objects
            .select_related("user")
            .get(pk=pk)
        )

    @staticmethod
    def delete_analysis(pk):

        analysis = (
            AnalysisHistory.objects.get(pk=pk)
        )

        analysis.delete()
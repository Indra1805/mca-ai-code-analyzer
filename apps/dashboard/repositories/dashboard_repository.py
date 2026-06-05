from django.db.models import Avg
from django.db.models import Count

from apps.code_analysis.models import (
    AnalysisHistory,
)


class DashboardRepository:

    @staticmethod
    def get_total_analyses(user):

        return (
            AnalysisHistory.objects
            .filter(user=user)
            .count()
        )

    @staticmethod
    def get_languages_used(user):

        return (
            AnalysisHistory.objects
            .filter(user=user)
            .values("language")
            .distinct()
            .count()
        )

    @staticmethod
    def get_average_confidence(user):

        result = (
            AnalysisHistory.objects
            .filter(user=user)
            .aggregate(
                avg_score=Avg(
                    "confidence_score"
                )
            )
        )

        return (
            round(
                result["avg_score"],
                2
            )
            if result["avg_score"]
            else 0
        )

    @staticmethod
    def get_recent_analyses(
        user,
        limit=5,
    ):

        return (
            AnalysisHistory.objects
            .filter(user=user)
            .order_by("-created_at")[:limit]
        )

    @staticmethod
    def get_most_used_language(user):

        result = (
            AnalysisHistory.objects
            .filter(user=user)
            .values("language")
            .annotate(
                total=Count("id")
            )
            .order_by("-total")
            .first()
        )

        return (
            result["language"]
            if result
            else "N/A"
        )
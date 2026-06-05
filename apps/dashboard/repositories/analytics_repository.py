from django.db.models import Avg
from django.db.models import Count

from apps.code_analysis.models import (
    AnalysisHistory,
)


class AnalyticsRepository:

    @staticmethod
    def language_distribution(user):

        return (
            AnalysisHistory.objects
            .filter(user=user)
            .values("language")
            .annotate(
                total=Count("id")
            )
            .order_by("-total")
        )

    @staticmethod
    def average_confidence(user):

        result = (
            AnalysisHistory.objects
            .filter(user=user)
            .aggregate(
                avg=Avg(
                    "confidence_score"
                )
            )
        )

        return result["avg"] or 0

    @staticmethod
    def average_duration(user):

        result = (
            AnalysisHistory.objects
            .filter(user=user)
            .aggregate(
                avg=Avg(
                    "analysis_duration_ms"
                )
            )
        )

        return result["avg"] or 0
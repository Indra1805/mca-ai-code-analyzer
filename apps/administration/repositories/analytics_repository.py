from datetime import timedelta

from django.db.models import Avg
from django.db.models import Count
from django.db.models import Sum
from django.utils import timezone

from apps.code_analysis.models import AnalysisHistory


class AnalyticsRepository:

    @staticmethod
    def language_distribution():

        return (
            AnalysisHistory.objects
            .values("language")
            .annotate(total=Count("id"))
            .order_by("-total")
        )

    @staticmethod
    def success_failure():

        return (
            AnalysisHistory.objects
            .values("analysis_status")
            .annotate(total=Count("id"))
            .order_by("analysis_status")
        )

    @staticmethod
    def average_confidence():

        return (
            AnalysisHistory.objects.aggregate(
                average=Avg("confidence_score")
            )["average"] or 0
        )

    @staticmethod
    def average_duration():

        return (
            AnalysisHistory.objects.aggregate(
                average=Avg("analysis_duration_ms")
            )["average"] or 0
        )

    @staticmethod
    def total_downloads():

        return (
            AnalysisHistory.objects.aggregate(
                total=Sum("report_download_count")
            )["total"] or 0
        )

    @staticmethod
    def recent_analysis_trend():

        today = timezone.now().date()

        data = []

        for i in range(6, -1, -1):

            day = today - timedelta(days=i)

            count = (
                AnalysisHistory.objects.filter(
                    created_at__date=day
                ).count()
            )

            data.append(
                {
                    "date": day.strftime("%d %b"),
                    "count": count,
                }
            )

        return data
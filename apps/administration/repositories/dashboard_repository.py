from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Sum

from apps.code_analysis.models import AnalysisHistory


User = get_user_model()


class DashboardRepository:

    @staticmethod
    def get_total_users():

        return User.objects.count()

    @staticmethod
    def get_total_analyses():

        return AnalysisHistory.objects.count()

    @staticmethod
    def get_successful_analyses():

        return AnalysisHistory.objects.filter(
            analysis_status=AnalysisHistory.AnalysisStatus.SUCCESS
        ).count()

    @staticmethod
    def get_failed_analyses():

        return AnalysisHistory.objects.filter(
            analysis_status=AnalysisHistory.AnalysisStatus.FAILED
        ).count()

    @staticmethod
    def get_average_confidence():

        return (
            AnalysisHistory.objects.aggregate(
                average=Avg(
                    "confidence_score"
                )
            )["average"]
            or 0
        )

    @staticmethod
    def get_average_duration():

        return (
            AnalysisHistory.objects.aggregate(
                average=Avg(
                    "analysis_duration_ms"
                )
            )["average"]
            or 0
        )

    @staticmethod
    def get_total_downloads():

        return (
            AnalysisHistory.objects.aggregate(
                total=Sum(
                    "report_download_count"
                )
            )["total"]
            or 0
        )

    @staticmethod
    def get_most_used_language():

        language = (
            AnalysisHistory.objects.values(
                "language"
            )
            .annotate(
                total=Count("id")
            )
            .order_by("-total")
            .first()
        )

        if language:

            return language["language"]

        return "-"
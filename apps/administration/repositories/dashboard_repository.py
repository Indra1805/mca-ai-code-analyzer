from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Sum
from django.db.models import Q

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



class UserRepository:

    @staticmethod
    def get_users(
        search=None,
        status=None,
    ):

        queryset = (
            User.objects
            .annotate(
                analysis_count=Count(
                    "analyses"
                )
            )
            .order_by(
                "-created_at"
            )
        )

        if search:

            queryset = queryset.filter(
                Q(username__icontains=search)
                |
                Q(email__icontains=search)
                |
                Q(first_name__icontains=search)
                |
                Q(last_name__icontains=search)
            )

        if status == "active":

            queryset = queryset.filter(
                is_active=True
            )

        elif status == "inactive":

            queryset = queryset.filter(
                is_active=False
            )

        return queryset

    @staticmethod
    def get_user(pk):

        return (
            User.objects
            .annotate(
                analysis_count=Count(
                    "analyses"
                )
            )
            .get(pk=pk)
        )
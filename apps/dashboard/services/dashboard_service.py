from apps.dashboard.repositories.dashboard_repository import (
    DashboardRepository,
)

from apps.dashboard.repositories.analytics_repository import (
    AnalyticsRepository,
)

from apps.dashboard.services.chart_service import (
    ChartService,
)


class DashboardService:

    @staticmethod
    def get_dashboard_data(user):

        return {

            "total_analyses":
                DashboardRepository.get_total_analyses(
                    user
                ),

            "languages_used":
                DashboardRepository.get_languages_used(
                    user
                ),

            "average_confidence":
                AnalyticsRepository.average_confidence(
                    user
                ),

            "average_duration":
                AnalyticsRepository.average_duration(
                    user
                ),

            "most_used_language":
                DashboardRepository.get_most_used_language(
                    user
                ),

            "recent_analyses":
                DashboardRepository.get_recent_analyses(
                    user
                ),

            "language_distribution":
                AnalyticsRepository.language_distribution(
                    user
                ),

            "language_chart":
                ChartService
                .get_language_chart_data(
                    user
                ),

            "status_chart":
                ChartService
                .get_status_chart_data(
                    user
                ),
        }
from apps.administration.repositories.analytics_repository import (
    AnalyticsRepository,
)


class AnalyticsService:

    @staticmethod
    def get_analytics():

        language = (
            AnalyticsRepository.language_distribution()
        )

        status = (
            AnalyticsRepository.success_failure()
        )

        trend = (
            AnalyticsRepository.recent_analysis_trend().__reversed__()
        )

        return {

            "language_distribution": language,

            "status_distribution": status,

            "average_confidence":
                AnalyticsRepository.average_confidence(),

            "average_duration":
                AnalyticsRepository.average_duration(),

            "total_downloads":
                AnalyticsRepository.total_downloads(),

            "trend": trend,

        }
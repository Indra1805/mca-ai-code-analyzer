from apps.administration.repositories.dashboard_repository import (
    DashboardRepository,
)


class DashboardService:

    @staticmethod
    def get_dashboard_data():

        return {

            "total_users":
                DashboardRepository.get_total_users(),

            "total_analyses":
                DashboardRepository.get_total_analyses(),

            "successful_analyses":
                DashboardRepository.get_successful_analyses(),

            "failed_analyses":
                DashboardRepository.get_failed_analyses(),

            "average_confidence":
                DashboardRepository.get_average_confidence(),

            "average_duration":
                DashboardRepository.get_average_duration(),

            "total_downloads":
                DashboardRepository.get_total_downloads(),

            "most_used_language":
                DashboardRepository.get_most_used_language(),

        }
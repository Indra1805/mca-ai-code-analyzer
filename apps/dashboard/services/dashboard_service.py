class DashboardService:

    @staticmethod
    def get_dashboard_data(user):

        return {
            "total_analyses": 0,
            "languages_used": 0,
            "reports_created": 0,
        }
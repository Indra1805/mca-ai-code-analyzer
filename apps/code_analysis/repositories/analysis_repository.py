from apps.code_analysis.models import AnalysisHistory


class AnalysisRepository:

    @staticmethod
    def create_analysis(**kwargs):
        return AnalysisHistory.objects.create(
            **kwargs
        )

    @staticmethod
    def get_user_analyses(user):
        return (
            AnalysisHistory.objects
            .filter(user=user)
            .order_by("-created_at")
        )

    @staticmethod
    def get_analysis_by_id(pk):
        return (
            AnalysisHistory.objects
            .filter(id=pk)
            .first()
        )
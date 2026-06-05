from django.urls import path

from . import views

app_name = "code_analysis"

urlpatterns = [
    path(
        "analyze/",
        views.analyze_code_view,
        name="analyze",
    ),

    path(
        "history/",
        views.analysis_history_view,
        name="history",
    ),

    path(
        "<int:analysis_id>/",
        views.analysis_detail_view,
        name="detail",
    ),

    path(
        "delete/<int:analysis_id>/",
        views.delete_analysis_view,
        name="delete",
    ),
]
from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path(
        "<int:analysis_id>/download/",
        views.download_report_view,
        name="download",
    ),
]
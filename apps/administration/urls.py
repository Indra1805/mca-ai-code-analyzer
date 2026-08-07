from django.urls import path

from . import views

app_name = "administration"

urlpatterns = [

    path(
        "",
        views.dashboard_view,
        name="dashboard",
    ),

    path(
        "users/",
        views.users_view,
        name="users",
    ),

    path(
        "users/<int:pk>/",
        views.user_detail_view,
        name="user_detail",
    ),

    path(
        "analyses/",
        views.analyses_view,
        name="analyses",
    ),

    path(
        "analyses/<int:pk>/",
        views.analysis_detail_view,
        name="analysis_detail",
    ),

    path(
        "analyses/<int:pk>/delete/",
        views.delete_analysis_view,
        name="delete_analysis",
    ),

    path(
        "analytics/",
        views.analytics_view,
        name="analytics",
    ),

]
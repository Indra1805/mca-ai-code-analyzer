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

]
"""
Views for dashboard module.
"""

from django.contrib.auth.decorators import (
    login_required,
)

from django.shortcuts import render

from .services.dashboard_service import (
    DashboardService,
)


@login_required(
    login_url="accounts:login"
)
def home(request):

    context = (
        DashboardService
        .get_dashboard_data(
            request.user
        )
    )

    return render(
        request,
        "dashboard/home.html",
        context,
    )
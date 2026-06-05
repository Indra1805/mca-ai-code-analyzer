from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services.dashboard_service import DashboardService

"""
Views for dashboard module.
"""


@login_required
def home(request):

    context = DashboardService.get_dashboard_data(
        request.user
    )

    return render(
        request,
        "dashboard/home.html",
        context,
    )
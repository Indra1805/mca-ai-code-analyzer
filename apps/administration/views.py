from django.contrib.admin.views.decorators import (
    staff_member_required,
)
from django.shortcuts import render

from apps.administration.services.dashboard_service import (
    DashboardService,
)


@staff_member_required
def dashboard_view(request):

    context = (
        DashboardService
        .get_dashboard_data()
    )

    return render(
        request,
        "administration/dashboard.html",
        context,
    )
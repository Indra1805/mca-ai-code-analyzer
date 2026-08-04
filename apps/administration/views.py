from django.contrib.admin.views.decorators import (
    staff_member_required,
)
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.contrib.auth import get_user_model

from apps.administration.services.dashboard_service import (
    DashboardService, UserService,
)

User = get_user_model()


@staff_member_required
def dashboard_view(request):

    context = DashboardService.get_dashboard_data()

    return render(
        request,
        "administration/dashboard.html",
        context,
    )


@staff_member_required
def users_view(request):

    search = request.GET.get(
        "search",
        ""
    )

    status = request.GET.get(
        "status",
        ""
    )

    users = UserService.get_users(
        search=search,
        status=status,
    )

    return render(
        request,
        "administration/users.html",
        {
            "users": users,
            "search": search,
            "status": status,
        },
    )


@staff_member_required
def user_detail_view(
    request,
    pk,
):

    user = get_object_or_404(
        User,
        pk=pk,
    )

    return render(
        request,
        "administration/user_detail.html",
        {
            "profile_user": user,
        },
    )
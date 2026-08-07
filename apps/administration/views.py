from django.contrib.admin.views.decorators import (
    staff_member_required,
)
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django.contrib.auth import get_user_model

from apps.administration.services.dashboard_service import (
    DashboardService, UserService,
)

from django.contrib import messages
from django.shortcuts import redirect

from apps.administration.services.analysis_service import (
    AnalysisService,
)

from apps.code_analysis.models import AnalysisHistory

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



@staff_member_required
def analyses_view(request):

    search = request.GET.get(
        "search",
        "",
    )

    language = request.GET.get(
        "language",
        "",
    )

    status = request.GET.get(
        "status",
        "",
    )

    analyses = (
        AnalysisService.get_analyses(
            search=search,
            language=language,
            status=status,
        )
    )

    return render(
        request,
        "administration/analyses.html",
        {
            "analyses": analyses,
            "languages": AnalysisHistory.LanguageChoices,
            "search": search,
            "language": language,
            "status": status,
        },
    )


@staff_member_required
def analysis_detail_view(
    request,
    pk,
):

    analysis = (
        AnalysisService.get_analysis(pk)
    )

    return render(
        request,
        "administration/analysis_detail.html",
        {
            "analysis": analysis,
        },
    )


@staff_member_required
def delete_analysis_view(
    request,
    pk,
):

    AnalysisService.delete_analysis(pk)

    messages.success(
        request,
        "Analysis deleted successfully.",
    )

    return redirect(
        "administration:analyses"
    )
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from apps.code_analysis.forms import (
    CodeAnalysisForm,
)

from apps.code_analysis.models import (
    AnalysisHistory,
)

from apps.code_analysis.services.analysis_service import (
    AnalysisService,
)

# Create your views here.


@login_required(login_url="accounts:login")
def analyze_code_view(request):

    if request.method == "POST":

        form = CodeAnalysisForm(
            request.POST
        )

        if form.is_valid():

            service = AnalysisService()

            analysis_data = (
                service.analyze_code(
                    user=request.user,
                    language=form.cleaned_data[
                        "language"
                    ],
                    code=form.cleaned_data[
                        "source_code"
                    ],
                )
            )

            messages.success(
                request,
                "Code analyzed successfully."
            )

            return redirect(
                "code_analysis:detail",
                analysis_data[
                    "analysis"
                ].id,
            )

    else:

        form = CodeAnalysisForm()

    return render(
        request,
        "code_analysis/analyze.html",
        {
            "form": form
        },
    )


@login_required(login_url="accounts:login")
def analysis_history_view(request):

    analyses = (
        AnalysisHistory.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    return render(
        request,
        "code_analysis/history.html",
        {
            "analyses": analyses
        },
    )


@login_required(login_url="accounts:login")
def analysis_detail_view(
    request,
    analysis_id,
):

    analysis = get_object_or_404(
        AnalysisHistory,
        id=analysis_id,
        user=request.user,
    )

    return render(
        request,
        "code_analysis/detail.html",
        {
            "analysis": analysis
        },
    )
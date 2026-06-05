from django.shortcuts import render
from django.contrib.auth.decorators import (
    login_required,
)

from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
)

from apps.code_analysis.models import (
    AnalysisHistory,
)

from .services.pdf_report_service import (
    PDFReportService,
)

# Create your views here.


@login_required(
    login_url="accounts:login"
)
def download_report_view(
    request,
    analysis_id,
):

    analysis = (
        get_object_or_404(
            AnalysisHistory,
            id=analysis_id,
            user=request.user,
        )
    )

    analysis.report_download_count += 1

    analysis.save(
        update_fields=[
            "report_download_count"
        ]
    )

    pdf = (
        PDFReportService
        .generate_analysis_report(
            analysis
        )
    )

    response = HttpResponse(
        pdf,
        content_type="application/pdf",
    )

    response[
        "Content-Disposition"
    ] = (
        f'attachment; '
        f'filename="analysis_{analysis.id}.pdf"'
    )

    return response
from django import forms

from apps.code_analysis.models import (
    AnalysisHistory
)


class CodeAnalysisForm(forms.Form):

    language = forms.ChoiceField(
        choices=(
            AnalysisHistory
            .LanguageChoices
            .choices
        )
    )

    source_code = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 15
            }
        )
    )
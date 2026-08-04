from django import forms

from apps.code_analysis.models import AnalysisHistory


class CodeAnalysisForm(forms.Form):
    """
    Form for submitting source code for AI analysis.
    """

    language = forms.ChoiceField(
        label="Programming Language",
        choices=AnalysisHistory.LanguageChoices.choices,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    source_code = forms.CharField(
        label="Source Code",
        widget=forms.Textarea(
            attrs={
                "class": "form-control code-editor",
                "id": "sourceCode",
                "spellcheck": "false",
                "placeholder": "Paste or type your source code here...",
            }
        ),
    )
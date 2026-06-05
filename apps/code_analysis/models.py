from django.conf import settings
from django.db import models

# Create your models here.


class AnalysisHistory(models.Model):
    """
    Stores code analysis results.
    """

    class LanguageChoices(models.TextChoices):
        PYTHON = "Python", "Python"
        JAVA = "Java", "Java"
        C = "C", "C"
        CPP = "C++", "C++"
        JAVASCRIPT = "JavaScript", "JavaScript"
        GO = "Go", "Go"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="analyses",
    )

    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
    )

    source_code = models.TextField()

    detected_errors = models.TextField()

    explanation = models.TextField()

    corrected_code = models.TextField()

    best_practices = models.TextField()

    confidence_score = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "analysis_history"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.user.username}"
            f" - {self.language}"
        )
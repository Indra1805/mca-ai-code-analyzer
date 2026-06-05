from dataclasses import dataclass


@dataclass
class AnalysisResult:

    language: str

    detected_errors: str

    explanation: str

    corrected_code: str

    best_practices: str

    confidence_score: int
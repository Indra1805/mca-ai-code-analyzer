"""
Gemini API integration service.
"""

import logging

import google.generativeai as genai

from django.conf import settings

logger = logging.getLogger(__name__)


class GeminiService:
    """
    Handles communication with Gemini.
    """

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            settings.GEMINI_MODEL
        )

    def generate_content(
        self,
        prompt: str,
    ) -> str:
        """
        Send prompt to Gemini and return response.
        """

        try:

            response = (
                self.model.generate_content(
                    prompt
                )
            )

            if not response.text:

                raise RuntimeError(
                    "Gemini returned empty response."
                )

            return response.text

        except Exception as exc:

            logger.exception(
                f"Gemini API Error: {exc}"
            )

            raise RuntimeError(
                "Unable to analyze code."
            ) from exc
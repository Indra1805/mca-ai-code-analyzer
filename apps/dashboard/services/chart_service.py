"""
Dashboard chart service.
"""

from apps.dashboard.repositories.analytics_repository import (
    AnalyticsRepository,
)

import json


class ChartService:

    @staticmethod
    def get_language_chart_data(
        user,
    ):

        data = (
            AnalyticsRepository
            .language_distribution(
                user
            )
        )

        labels = []
        values = []

        for item in data:

            labels.append(
                item["language"]
            )

            values.append(
                item["total"]
            )

        return {
            "labels": json.dumps(
                labels
            ),
            "values": json.dumps(
                values
            ),
        }
    

    @staticmethod
    def get_status_chart_data(
        user,
    ):

        data = (
            AnalyticsRepository
            .status_distribution(
                user
            )
        )

        labels = []
        values = []

        for item in data:

            labels.append(
                item[
                    "analysis_status"
                ]
            )

            values.append(
                item["total"]
            )

        return {
            "labels":
                json.dumps(
                    labels
                ),

            "values":
                json.dumps(
                    values
                ),
        }
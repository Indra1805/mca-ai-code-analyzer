import re


class JSONCleaner:

    @staticmethod
    def clean(
        response_text: str
    ):

        response_text = (
            response_text.strip()
        )

        response_text = re.sub(
            r"```json",
            "",
            response_text,
        )

        response_text = re.sub(
            r"```",
            "",
            response_text,
        )

        return response_text.strip()
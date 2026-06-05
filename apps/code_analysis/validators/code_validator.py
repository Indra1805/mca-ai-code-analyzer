class CodeValidator:

    MIN_LENGTH = 10

    MAX_LENGTH = 10000

    @classmethod
    def validate(cls, code: str):

        if not code:
            raise ValueError(
                "Code cannot be empty."
            )

        if len(code) < cls.MIN_LENGTH:
            raise ValueError(
                "Code is too short."
            )

        if len(code) > cls.MAX_LENGTH:
            raise ValueError(
                "Code exceeds maximum size."
            )
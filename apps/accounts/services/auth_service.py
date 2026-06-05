from django.contrib.auth import authenticate


class AuthService:

    @staticmethod
    def authenticate_user(
        username: str,
        password: str,
    ):
        return authenticate(
            username=username,
            password=password,
        )
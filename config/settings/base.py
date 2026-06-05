from pathlib import Path
from dotenv import load_dotenv
import os

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --------------------------------------------------
# ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.common",
    "apps.accounts",
    "apps.code_analysis",
    "apps.dashboard",
    "apps.reports",
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = (
    DJANGO_APPS
    + LOCAL_APPS
    + THIRD_PARTY_APPS
)

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# URL CONFIG
# --------------------------------------------------

ROOT_URLCONF = "config.urls"

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates"
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = "config.wsgi.application"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------------------------------------
# PASSWORD VALIDATORS
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "DENY"

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------------------------
# MEDIA FILES
# --------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# GEMINI
# --------------------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# LOGGING
# --------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs/application.log",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

AUTH_USER_MODEL = "accounts.User"



LOGIN_URL = "accounts:login"

LOGIN_REDIRECT_URL = "dashboard:home"

LOGOUT_REDIRECT_URL = "accounts:login"


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "models/gemini-2.5-flash"
)
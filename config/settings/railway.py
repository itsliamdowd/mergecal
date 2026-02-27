from .base import *  # noqa
from .base import env

# SECURITY
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[".up.railway.app"])

# DATABASE
DATABASES["default"] = env.db("DATABASE_URL")  # noqa: F405

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY
CELERY_BROKER_URL = env("REDIS_URL")
CELERY_RESULT_BACKEND = env("REDIS_URL")

SECURE_SSL_REDIRECT = False

# STATIC FILES - serve locally, no AWS needed
STATIC_URL = "/static/"
STATIC_ROOT = "/app/staticfiles"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# EMAIL - console for now
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# STRIPE - not needed for personal use
STRIPE_SECRET_KEY = ""
STRIPE_PUBLISHABLE_KEY = ""

# SECURITY SETTINGS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

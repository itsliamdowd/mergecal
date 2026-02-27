from .production import *  # noqa

# Override storage to use local files instead of AWS S3
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Disable AWS requirement
AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_STORAGE_BUCKET_NAME = None

# Disable Stripe requirement  
STRIPE_SECRET_KEY = ""
STRIPE_PUBLISHABLE_KEY = ""

# Use console email backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

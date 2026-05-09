from pathlib import Path
import os
from dotenv import load_dotenv
from django.urls import reverse_lazy
import sys

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG").lower()=="true"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework'    
]

LOCAL_APPS = [
    'accounts',
    'api',
    'blog',
    'core',
    'q_a',
    'cart',
    'formsaz'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = "accounts.Account"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

LANGUAGE_CODE = 'fa-IR'

TIME_ZONE = 'Asia/tehran'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = reverse_lazy("accounts:me")
LOGIN_URL = reverse_lazy("accounts:login")

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
}


class Exclude2xxFilter:
    def filter(self, record):
        msg = record.getMessage()
        if '"] ' in msg:
            status_code_str = msg.split('"] ')[1].split(' ')[0]
            try:
                status_code = int(status_code_str)
                if 100 <= status_code < 300:
                    return True
            except ValueError:
                pass
        return False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'exclude_2xx': {
            '()': Exclude2xxFilter,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'style': '%',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
            'style': '%',
        },
        'access': {
            'format': '"%(asctime)s %(levelname)s %(name)s %(message)s"',
            'style': '%',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
        'access_log_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'access',
            'filters': ['exclude_2xx'],
            'stream': sys.stdout,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['access_log_handler'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
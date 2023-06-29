"""
Django settings for PurBeurre project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
import os
import django_heroku
import dj_database_url
from dj_database_url import parse as db_url
import json
# import psycopg2.extensions
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

config = {}
location = Path(__file__).absolute().parent / "config.json"

with open(location) as file:
    config = json.loads(file.read())


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['beurrepur.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    "foodfacts",
    "roles",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "PurBeurre.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR + "/foodfacts", "templates"),
                 os.path.join(BASE_DIR + "/roles", "templates"),
                 os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    "roles.EmailBackend.EmailBackend",
    "django.contrib.auth.backends.AllowAllUsersModelBackend"]

WSGI_APPLICATION = "PurBeurre.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE":  config['ENGINE'],
        "OPTIONS": {},
        "NAME": config['DB_NAME'],
        "USER": config['DB_USER'],
        "PASSWORD": config['DB_PASSWORD'],
        "HOST": config['DB_HOST'],
        "PORT": config['DB_PORT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
                "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATIC_URL = "/static/"

# Activate Django-Heroku.
django_heroku.settings(locals())

# Email
EMAIL_BACKEND = config['EMAIL_BACKEND']
EMAIL_HOST = "mail53.lwspanel.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "cedric@trackon-music.com"
EMAIL_HOST_PASSWORD = ""
# EMAIL_HOST = "smtp.mailgun.org"
# EMAIL_PORT =  config['EMAIL_PORT']
# EMAIL_HOST_USER = config["EMAIL_HOST_USER"]
EMAIL_USE_SSL = config["EMAIL_USE_SSL"]
EMAIL_USE_TLS = config["EMAIL_USE_TLS"]
# EMAIL_HOST_PASSWORD = config["EMAIL_HOST_PASSWORD"]
#EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
#DEFAULT_FROM_EMAIL = config['DEFAULT_FROM_EMAIL']

# redirection
LOGIN_URL = config['LOGIN_URL']
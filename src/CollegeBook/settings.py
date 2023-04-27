"""
Django settings for CollegeBook project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2)6^n^(9nzbp22r4-=!anhuqfuct43$=nuud9-%#*v27yk)%(w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tagify',
    'Account',
    'Event',
    'Configuration',
    'Reservation',
    'Payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CollegeBook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'CollegeBook/templates',
            BASE_DIR / 'Account/templates',
            BASE_DIR / 'Event/templates',
            BASE_DIR / 'Configuration/templates',
            BASE_DIR / 'Reservation/templates',
            BASE_DIR / 'Payment/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CollegeBook.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Authentication class
AUTH_USER_MODEL = 'Account.User'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "CollegeBook/static",
    BASE_DIR / "Event/static",
    BASE_DIR / "Configuration/static",
    BASE_DIR / "Reservation/static",
    BASE_DIR / "Payment/static",
]

MEDIA_URL = "Media/"

MEDIA_ROOT = BASE_DIR / "CollegeBook/Media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DOMAIN = "http://localhost:8000/"

STRIPE_PUBLIC_KEY = "pk_test_51My9egKzH6J7qKOAvja1Gc7MAjiYmhRWeoCW25bXv2ymkb4wDUrSMWkWPUdH82GizI7esBI6UUyXLDEgbUxZYVHI00aIBswFkO"
STRIPE_SECRET_KEY = "sk_test_51My9egKzH6J7qKOAtpIjOzmEUcP5mHkvejI1syfp7t9konG7teSXWwXl88yTdA3Wtx5UT6wOiuy4TEVjrB4k3o9j00FEtHZOC6"
STRIPE_ENDPOINT_SECRET = "whsec_0f4a1af15fa5c6f432602f48bb6cb05dbcfbae36733e61e6adbfa8cddffe2507"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'collegebooktest@gmail.com'
EMAIL_HOST_PASSWORD = 'bukbfkukzqosrqcu'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
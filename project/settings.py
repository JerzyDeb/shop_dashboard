"""Settings file."""

# Standard Library
import os
from pathlib import Path

# 3rd-party
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# SETTING DEBUG & SECRET KEY
DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env.str('SECRET_KEY')

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASS'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.str('DATABASE_PORT'),
    }
}

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # local
    'my_apps.core',
    'my_apps.dashboard',
    'my_apps.shop',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Debug Settings
if DEBUG:
    ALLOWED_HOSTS = ['*'] + env.list('ALLOWED_HOSTS')
    CSRF_TRUSTED_ORIGINS = [
        'http://0.0.0.0:8000',
        'http://127.0.0.1:8000',
        f'https://{env.str("DOMAIN")}',
    ]
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
    CSRF_TRUSTED_ORIGINS = [f'https://{env.str("DOMAIN")}']
    RECAPTCHA_PUBLIC_KEY = '6Lc-t7kZAAAAAK5zUXNrROgCAAr3kE4HOadRgYDw'
    RECAPTCHA_PRIVATE_KEY = '6Lc-t7kZAAAAAJV_WdO9Zk-nSDBlMne9VdsrdUUU'
    INSTALLED_APPS += ['elasticapm.contrib.django']
    TEMPLATES[0]['OPTIONS']['context_processors'] += [
        'elasticapm.contrib.django.context_processors.rum_tracing'
    ]
    ELASTIC_APM = {
        'SERVICE_NAME': env('APP'),
        'ENVIRONMENT': env('ENV_VERSION'),
        'SERVER_URL': 'https://apm.cloudformers.pl',
        'ACTIVE': 'True',
        'DEBUG': 'True',
    }

# Password validation
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


# Internationalization
LANGUAGE_CODE = 'pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'apps_static/')
# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL')
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL')
EMAIL_PORT = env.str('EMAIL_PORT')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

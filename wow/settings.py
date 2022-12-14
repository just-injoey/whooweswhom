"""
Django settings for wow project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4gm$^^_pw*sd)gsachu96nt26l)kcaz5i3&2141xi#1oxjk760'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://whooweswhom-production.up.railway.app','https://*.127.0.0.1']
# ALLOWED_HOSTS = ['web-production-1afb.up.railway.app']
# ALLOWED_HOSTS = ['web-production-60e5.up.railway.app']
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'splitter',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

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

AUTH_USER_MODEL = 'splitter.User'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   "allauth.account.auth_backends.AuthenticationBackend",
)


SITE_ID = 2

LOGIN_REDIRECT_URL = "/"



SOCIALACCOUNT_PROVIDERS = {
"google": {
    "APP": {
        "client_id": "788851246302-isb6ahrlrvhisvrq3bmuekjq9jr74f0h.apps.googleusercontent.com",
        "secret": "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",
    },
},
}

# SOCIALACCOUNT_PROVIDERS = {
# "google": {
#     "APP": {
#         "client_id": "947250457248-oo6m984j7hl99jvjeha24hgqkkkeuim9.apps.googleusercontent.com",
#         "secret": "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",
#     },
# },
# }

# SOCIALACCOUNT_PROVIDERS = {
#    'google': {
#       'APP':{
#         'client_id': os.environ['947250457248-oo6m984j7hl99jvjeha24hgqkkkeuim9.apps.googleusercontent.com'],
#         'secret': os.environ['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'],
#       }
#    }
# }
# SOCIALACCOUNT_PROVIDERS = {
#    'google': {
#       'SCOPE': [
#          'profile',
#          'email',
#       ],
#       'AUTH_PARAMS': {
#          'access_type': 'online',
#       }
#    }
# }


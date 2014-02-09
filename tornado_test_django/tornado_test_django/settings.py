"""
Django settings for tornado_test_django project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's24fdzk^c+3nw*8zj2(t59x73^bj@7dwfp5**8qs)1z9^pd$^^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [*]

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

DEFAULT_INDEX_TABLESPACE = 'lunch_crew'
DEFAULT_TABLESPACE = 'lunch_crew'
TRANSACTIONS_MANAGED = True
FORCE_SCRIPT_NAME = True
DEBUG_PROPAGATE_EXCEPTIONS = True
SESSION_COOKIE_NAME = 'lunch_crew'
SESSION_CACHE_ALIAS = 'default'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
DISALLOWED_USER_AGENTS = ()
USE_X_FORWARDED_HOST = False
PREPEND_WWW = False
APPEND_SLASH = False
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lunch_crew',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tornado_test_django.urls'

WSGI_APPLICATION = 'tornado_test_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

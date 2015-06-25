"""
Django settings for migreat2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
from django.conf import settings
import dj_database_url
import os.path

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@)oc2=a+(_9!9k=(uv&%g$u8w1p@t&r&#p(8ju=0htic5epp$v'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

PROJECT_DIR = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    root('templates'),
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

ALLOWED_HOSTS = [".herokuapp.com"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'peer_app',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# LOGIN_URL = 'mysite_login'
# LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/main/'

ROOT_URLCONF = 'migreat2.urls'

WSGI_APPLICATION = 'migreat2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# DATABASES = {
#     'default': dj_database_url.config(default='postgres://<user>:<password>@<host>/<dbname>')
# }

# DATABASES['default'] =  dj_database_url.config()
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'migreattwo',
#         'USER': '',                     
#         'PASSWORD': '',                  
#         'HOST': '',                      
#         'PORT': '',        
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# SITE_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = (
#   os.path.join(SITE_ROOT, 'static/'),
# )



import os
from django.conf.global_settings import *

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
SITE_ID = 1

USE_I18N = False
USE_L10N = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/static'

ROOT_URLCONF = 'hubsite.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'hubsite.context_processors.debug_mode',
    'django.contrib.messages.context_processors.messages'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

EMAIL_HOST = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25

CONTACT_US_EMAILS = (
    'info@scrapinghub.com',
)

try:
    from local_settings import *
except ImportError:
    pass

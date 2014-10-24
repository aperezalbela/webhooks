# This file is deployed by APT and not recommended to be modified manually.
# Instead, add a /etc/hubsite/server_settings.py file for your custom
# settings.

import socket

DEBUG = False

MAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[hubsite] '
SERVER_EMAIL = 'hubsite@%s' % socket.getfqdn()
ADMINS = [('Errors', 'errors@scrapinghub.com')]

# hubsite doesn't require a database (yet)
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = '/var/lib/hubsite/hubsite.db'
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''

TEMPLATE_DIRS = ['/usr/share/hubsite/templates']
MEDIA_ROOT = '/usr/share/hubsite/media'

try:
    from server_settings import *
except ImportError:
    pass

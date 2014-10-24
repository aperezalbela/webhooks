import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'hubsite.settings'
sys.path.append('/etc/hubsite')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

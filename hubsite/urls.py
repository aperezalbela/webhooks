from django.conf import settings
from django.conf.urls import url, patterns, include

urlpatterns = patterns('',
    url(r'^$', 'webhooks.views.getrequest', name='getrequest'),    
)

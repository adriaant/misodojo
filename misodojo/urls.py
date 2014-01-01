# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

#==============================================================================
# Application
#==============================================================================

urlpatterns = patterns('',
    # pages
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name="home"),

    # grappelli
    url(r'^grappelli/', include('grappelli.urls')),

    # admin tool
    url(r'^admin/', include(admin.site.urls)),

    # apps
    url(r'^blog/', include('blog.urls')),

    # flatpages. Use this method, not documented method (commented out)
    # so we can use reverse urls such as e.g. {% url 'flatpage' url='/about/' %}
    url(r'^pages(?P<url>.*)$', 'django.contrib.flatpages.views.flatpage', name='flatpage'),
    #url(r'^pages/', include('django.contrib.flatpages.urls')),
)

#==============================================================================
# Serving static files during development (only in debug mode)
#==============================================================================

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

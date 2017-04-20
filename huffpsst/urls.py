# -*- coding: utf-8 -*-
import os.path

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch.urls import frontend as wagtailsearch_frontend_urls


admin.autodiscover()

handler404 = 'huffpsst.views.errors.error404'
handler403 = 'huffpsst.views.errors.error403'
handler500 = 'huffpsst.views.errors.error500'


# Signal handlers
from wagtail.wagtailsearch import register_signal_handlers as wagtailsearch_register_signal_handlers
wagtailsearch_register_signal_handlers()


urlpatterns = patterns('',
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_frontend_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^redactor/', include('redactor.urls')),
    url('^markdown/', include('django_markdown.urls')),
    url('^markdown/', include('django_markdown.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}),
    )







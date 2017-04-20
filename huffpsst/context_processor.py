from django.conf import settings
from django.contrib.sites.models import Site

__author__ = 'jawache'


def template_settings(request):
    return {
        'SETTINGS':settings,
        'SITE':Site.objects.get_current(),
        'HARVARD_URL': settings.LAMPOON,
    }


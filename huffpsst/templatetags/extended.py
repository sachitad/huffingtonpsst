# -*- coding: utf-8 -*-

# MAKE SURE
#
# TEMPLATE_CONTEXT_PROCESSORS has "django.core.context_processors.request",
import json
import locale

from django.template import Library
from django.template.defaultfilters import time, stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import markdown


register = Library()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

@register.simple_tag
def divide(value, arg): return int(float(value) / float(arg))


@register.simple_tag
def active(request, pattern):
    import re

    if re.search(pattern, request.path):
        return 'active'
    return ''

def jsonify(object):
    return json.dumps(object)

register.filter('jsonify', jsonify)


@register.filter
def epoch(value):
    try:
        return int(time.mktime(value.timetuple())*1000)
    except AttributeError:
        return ''

@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)


@register.filter(is_safe=True)
@stringfilter
def markdownRender(value):
    extensions = ["nl2br", ]

    return mark_safe(markdown.markdown(force_unicode(value),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))
from django import template

from advert.models import Advert

register = template.Library()


@register.assignment_tag()
def side_random_advert():
    return Advert.objects.filter(is_active=True, placement='Side').order_by('?')[:1]


@register.assignment_tag()
def header_random_advert():
    return Advert.objects.filter(is_active=True, placement='Header').order_by('?')[:1]
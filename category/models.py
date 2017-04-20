from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class Category(Page):
    show_in_sub_menu = models.BooleanField(default=False)

Category.content_panels = [
    FieldPanel('title', classname="title"),
]

Category.promote_panels = [
    FieldPanel('slug'),
    FieldPanel('seo_title'),
    FieldPanel('show_in_menus'),
    FieldPanel('show_in_sub_menu'),
    FieldPanel('search_description'),
]


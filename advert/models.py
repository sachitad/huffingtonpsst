from django.db import models

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from category.models import Category


class Advert(models.Model):
    placement_choices = (
        ('Header', 'Header'),
        ('Side', 'Side'),
        ('Footer', 'Footer'),
    )
    categories = models.ManyToManyField(Category)
    text = models.CharField(max_length=255)
    image = models.ForeignKey('wagtailimages.Image')
    custom_redirect_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    placement = models.CharField(choices=placement_choices, max_length=6, default='Side')

    panels = [
        FieldPanel('categories'),
        FieldPanel('text'),
        ImageChooserPanel('image'),
        FieldPanel('custom_redirect_url'),
        FieldPanel('placement'),
        FieldPanel('is_active'),
    ]

    def __unicode__(self):
        return self.text

register_snippet(Advert)
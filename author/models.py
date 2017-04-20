from django.db import models

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class Author(models.Model):
    name = models.CharField(max_length=255)
    short_bio = models.CharField(max_length=255)
    biography = RichTextField()
    is_active = models.BooleanField(default=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('short_bio'),
        FieldPanel('biography', classname="full"),
        FieldPanel('is_active'),
        ImageChooserPanel('image'),
    ]

    def __unicode__(self):
        return self.name

register_snippet(Author)
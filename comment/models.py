from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey


class Comment(models.Model):
    name = models.CharField(max_length=255, help_text='Commentator Name')
    bio = models.CharField(max_length=255, blank=True, null=True,
                           help_text='Short Bio of commentator (For example:  Nature Lover)')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, help_text='Only the comment marked as active will be shown')
    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
        FieldPanel('comment'),
        FieldPanel('is_active'),
    ]

    class Meta:
        abstract = True


# The real model which combines the abstract model, an Orderable helper class, and what amounts to a ForeignKey link
# to the model we want to add related links to (Article)
# Reference https://media.readthedocs.org/pdf/wagtail/latest/wagtail.pdf Pg: 31
class ArticleRelatedComments(Orderable, Comment):
    article = ParentalKey('article.Article', related_name='related_comments')

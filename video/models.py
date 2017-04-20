from django.db import models

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


from comment.models import Comment


class HuffingtonLivePage(Page):
    pass


HuffingtonLivePage.content_panels = [
    FieldPanel('title', classname="full title"),
]

HuffingtonLivePage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
]


class VideoTag(TaggedItemBase):
    content_object = ParentalKey('Video', related_name='tagged_items')


class Video(Page):
    youtube_link = models.URLField()
    tags = ClusterTaggableManager(through=VideoTag, blank=True)
    created = models.DateTimeField(auto_now_add=True)

Video.content_panels = [
    FieldPanel('title'),
    FieldPanel('youtube_link'),
    FieldPanel('tags'),
]


class VideoComment(Comment):
    """
    This is a fixed set of comments created by the authors for the live screen (doesn't change per video)."""
    pass

    def __unicode__(self):
        return self.name


register_snippet(VideoComment)
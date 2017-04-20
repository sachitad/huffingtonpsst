from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from author.models import Author
from category.models import Category
from comment.models import ArticleRelatedComments


class ArticleTag(TaggedItemBase):
    content_object = ParentalKey('Article', related_name='tagged_items')


class Article(Page):
    author = models.ForeignKey(Author)
    body = RichTextField()
    tags = ClusterTaggableManager(through=ArticleTag, blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    is_blog = models.BooleanField(default=False)
    is_top_post = models.BooleanField(default=False)
    is_dirty_post = models.BooleanField(default=False, help_text="Check the box if cleaning is allowed in this article.")
    custom_redirect_url = models.URLField(help_text='Custom Redirect URL for Read More', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


Article.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    FieldPanel('tags'),
    ImageChooserPanel('featured_image'),
    FieldPanel('is_blog'),
    FieldPanel('is_dirty_post'),
    FieldPanel('is_top_post'),
    FieldPanel('custom_redirect_url'),
    FieldPanel('author'),
    InlinePanel(Article, 'related_comments', label='Comments'),

]

Article.promote_panels = [
    FieldPanel('slug'),
    FieldPanel('seo_title'),
    FieldPanel('show_in_menus'),
    FieldPanel('search_description'),
]



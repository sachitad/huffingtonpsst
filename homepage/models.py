from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel, FieldPanel, MultiFieldPanel, InlinePanel

from modelcluster.fields import ParentalKey


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('homepage.HomePage', related_name='related_links')


class HomePage(Page):
    main_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='main_link'
    )
    main_link_title = models.CharField(max_length=255, blank=True, null=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name = 'Homepage'

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    PageChooserPanel('main_link'),
    FieldPanel('main_link_title', classname="full title"),
    ImageChooserPanel('featured_image'),
    InlinePanel(HomePage, 'related_links', label="Related links"),
]

HomePage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
]



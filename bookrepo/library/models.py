from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks


class AuthorPage(Page):
    template = "library/author_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
        ], use_json_field=True, null=True, blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Author Page"
        verbose_name_plural = "Author Pages"




class BookDirectory(Page):
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
        ], use_json_field=True, null=True, blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Book Page"
        verbose_name_plural = "Author Pages"

from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, BooleanBlock, ListBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()
    image_text = ImageText()
    image_block = ListBlock(ImageChooserBlock)

class TitleAndTextBlock(StructBlock):
    title = CharBlock(required=True, help_text='Add your title')
    text = CharBlock(required=True, help_text='add your additional text')

    class META:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "RichText"
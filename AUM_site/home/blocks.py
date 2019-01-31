from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class HeroBannerCarrousel(blocks.StructBlock):
    heading = blocks.RichTextBlock()
    image = ImageChooserBlock()


class Banner(blocks.StructBlock):
    type = blocks.ChoiceBlock(choices=[
    ('long', 'Long'),
    ('short', 'Short'),
], icon='edit')
    textType = blocks.ChoiceBlock(choices=[
        ('simple', 'Simple'),
        ('double', 'double'),
    ], icon='edit')
    text = blocks.RichTextBlock()
    text2 = blocks.RichTextBlock()

    class Meta:
        icon = 'user'
        form_classname = 'apply-banner struct-block'

    #def get_form_context(self, value, prefix='', errors=None):
    #    context = super().get_form_context(value, prefix=prefix, errors=errors)
    #    return context
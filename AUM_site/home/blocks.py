from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.blocks import SnippetChooserBlock


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
    tintBlue = blocks.FloatBlock(label='Alpha Tint of the Blue Overlay')


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


class CircleApplyWithPhoto(blocks.StructBlock):
    idHash = blocks.CharBlock(label='To be identified by script')
    image = ImageChooserBlock()


class VerticalSpace(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], icon='edit')


class ThreeColumnsMiniItem(blocks.StructBlock):
    text_top = blocks.RichTextBlock()
    type_text_top = blocks.ChoiceBlock(choices=[
        ('small', 'Small'),
        ('big', 'Big'),
    ], icon='edit')
    text_big = blocks.RichTextBlock()
    text_big_color = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
        ('cyan', 'Cyan'),
    ], icon='edit')
    text_mini = blocks.RichTextBlock()
    has_link = blocks.BooleanBlock(required=False)
    link = blocks.PageChooserBlock(blank=True, null=True)


class ThreeColumnsMini(blocks.StructBlock):
    column_one = ThreeColumnsMiniItem()
    column_two = ThreeColumnsMiniItem()
    column_three = ThreeColumnsMiniItem()

    class Meta:
        icon = 'placeholder'
        label = 'Three Columns Mini'


class MagicPinColor(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')
    trigger_hook = blocks.CharBlock(label="Value from 0 to 1 ej: 0.45, or events like onLeave, check Scrollmagic")
    duration = blocks.CharBlock(label="Duration in Pixels ej: 500, or % of screen")
    color_bg = SnippetChooserBlock('home.Colors', blank=True)
    push_followers = blocks.BooleanBlock(required=False)


class CentralCircle(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')
    font_color = SnippetChooserBlock('home.Colors', blank=True)
    back_color = SnippetChooserBlock('home.Colors', blank=True)
    text_big = blocks.RichTextBlock()
    text_line1 = blocks.RichTextBlock()
    text_line2 = blocks.RichTextBlock()


class CircleImageItem(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()

class CircleImageBlock(blocks.StructBlock):
    key = blocks.CharBlock(label='Id of object to use as activator')
    images = blocks.StreamBlock([
        ('image', CircleImageItem())
    ], null=True, blank=True)


class BigTextBoxesItem(blocks.StructBlock):
    has_link = blocks.BooleanBlock(required=False)
    link = blocks.PageChooserBlock(blank=True, null=True)
    text = blocks.RichTextBlock();


class BigTextBoxes(blocks.StructBlock):
    boxes = blocks.StreamBlock([
        ('box', BigTextBoxesItem())
    ], null=True, blank=True)

class CarouselWithBanner(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')
    text_big = blocks.RichTextBlock()
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    use_banner = blocks.BooleanBlock(required=False)
    use_button = blocks.BooleanBlock(required=False)
    link_button = blocks.PageChooserBlock(blank=True, null=True)
    button_text_big = blocks.CharBlock()
    button_text_line1 = blocks.CharBlock()
    button_text_line2 = blocks.CharBlock()
    text_line1 = blocks.RichTextBlock()
    use_round_effect = blocks.BooleanBlock(required=False)


class MagicCarouselUnround(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')





from django.db import models
from wagtail.core.models import Page
from wagtail.embeds import blocks

from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel,
                                         )
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from home.blocks import *
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.models import register_snippet



class HomePage(Page):
    description = models.CharField(max_length=255, blank=True, )

    herocarrousel = StreamField([('item', HeroBannerCarrousel())],null=True, blank=True)
    herobanner = StreamField([('item', Banner())], null=True, blank=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('circle_apply_with_photo', CircleApplyWithPhoto(icon="image")),
        ('central_circle', CentralCircle(icon="radio-empty")),
        ('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs",icon="site")),
    ], null=True, blank=True)

    effects = StreamField([
        ('pin_color', MagicPinColor()),
        ('unround_carousel', MagicCarouselUnround())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        MultiFieldPanel(
            [
                StreamFieldPanel('herocarrousel'),
                StreamFieldPanel('herobanner'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('body'),
            ],
            heading="Body",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('effects'),
            ],
            heading="Effects",
            classname="collapsible collapsed"
        ),

    ]

    def get_programs(self):
        return ProgramPage.objects.descendant_of(self).live()

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['programs'] = self.get_programs()
        context['home_page'] = self
        return context


class ProgramPage(Page):
    programTitle = models.CharField(max_length=255, blank=True, )
    group = models.CharField(max_length=255, blank=True, help_text='Use as: Bachelor of ....')
    letters = models.CharField(max_length=5, blank=True, )
    short = RichTextField( help_text='Short description to use in other pages');
    imageBase = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('programTitle', classname="full"),
        FieldPanel('group', classname="full"),
        FieldPanel('letters', classname="full"),
        FieldPanel('short', classname="full"),
        ImageChooserPanel('imageBase', classname="full"),

    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ProgramPage, self).get_context(request, *args, **kwargs)
        context['program_page'] = self
        return context


@register_setting
class ApplyBanner(BaseSetting):
    link = models.URLField(
        help_text='Apply Form Link')
    bigtext = models.CharField(
        max_length=255, help_text='The Big Text like APPLY NOW')
    useTwolines = models.BooleanField(default=True, help_text='If Show Two Lines of Text Bellow')
    line1 = models.CharField(
        max_length=255, help_text='Line One', default="")
    line2 = models.CharField(
        max_length=255, help_text='Line Two', default="")


@register_setting
class GlobalSettings(BaseSetting):
    logoTopGeneral = models.ImageField(help_text='The Logo For Top Left');


@register_snippet
class Colors(models.Model):
    name = models.CharField(max_length=255)

    color = models.CharField(max_length=7, help_text='Color in hexa #')

    panels = [
        FieldPanel('name'),
        FieldPanel('color'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"
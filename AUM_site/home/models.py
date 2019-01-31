from django.db import models
from wagtail.core.models import Page
from wagtail.embeds import blocks

from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from home.blocks import *

from wagtail.contrib.settings.models import BaseSetting, register_setting



class HomePage(Page):
    description = models.CharField(max_length=255, blank=True, )

    herocarrousel = StreamField([('item', HeroBannerCarrousel())],null=True, blank=True)
    herobanner = StreamField([('item', Banner())], null=True, blank=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        StreamFieldPanel('herocarrousel'),
        StreamFieldPanel('herobanner'),
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['home_page'] = self
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
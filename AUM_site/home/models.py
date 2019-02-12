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

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from blog.models import *




class HomePage(Page):
    description = models.CharField(max_length=255, blank=True, )

    #herocarrousel = StreamField([('item', HeroBannerCarrousel())],null=True, blank=True)
    #herobanner = StreamField([('item', Banner())], null=True, blank=True)

    herocarrousel = StreamField([
        ('multi', HeroCarouselMulti()),
        ('academic', HeroAcademic()),
        ('mini_photo', HeroWithMiniFoto()),
        ('solo_text', HeroSoloText()),
        ('photo_or_letters', HeroWithFotoOrLetter()),
        ('with_parameters', HeroParametric()),
    ], null=True, blank=True)

    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
                              ], null=True, blank=True)

    use_inverted_menu = models.BooleanField(default=False, help_text="Invert the color of the Top Menu")

    #body = StreamField([
    #    ('heading', blocks.CharBlock(classname="full title")),
    #    ('paragraph', blocks.RichTextBlock()),
    #    ('image', ImageChooserBlock(icon="image")),
    #    ('circle_apply_with_photo', CircleApplyWithPhoto(icon="image")),
    #    ('central_circle', CentralCircle(icon="radio-empty")),
    #    ('two_columns', TwoColumnBlock()),
    #    ('vertical_space', VerticalSpace()),
    #    ('circle_image_block', CircleImageBlock(icon="placeholder")),
    #    ('big_text_boxes', BigTextBoxes(icon="placeholder")),
    #    ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
    #    ('three_columns_mini', ThreeColumnsMini()),
    #    ('embedded_video', EmbedBlock(icon="media")),
    #    ('programs_list', blocks.StaticBlock(label="Show the list of Programs",icon="site")),
    #    ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post",icon="site")),
    #], null=True, blank=True)

    body = StreamField([
        #('heading', blocks.CharBlock(classname="full title")),
        #('paragraph', blocks.RichTextBlock()),
        #('image', ImageChooserBlock(icon="image")),
        ('circle_apply_with_photo', CircleApplyWithPhoto(icon="image")),
        ('central_circle', CentralCircle(icon="radio-empty")),
        #('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        #('embedded_video', EmbedBlock(icon="media")),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs", icon="site")),
        ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post", icon="site")),
        ('full_text', FullText()),
        ('fast_full_text', FastFullText()),
        ('two_columns_aum', TwoColumnAumGeneric()),
        ('separator_arrow', SeparatorLittleArrow()),
        ('circle_key_values', CircleKeyValues()),
        ('circle_apply_banner', CircleApplyBanner()),
        ('big_numbers_text', BigNumbersText()),
        ('group_cards', GroupCards()),
        ('two_columns_inverted', TwoColumnsInverted()),
        ('professor_list', MiniProfessorList()),
        ('round_frame_text', RoundFrameText()),
        ('vertical_paragraph', VerticalParagraph()),
        ('vertical_paragraph_complex', VerticalParagraphComp()),
        ('mini_apply_alone', MiniApplyAlone()),
        ('anchor', AnchorBlock()),
        ('generic_button', GenericButtonAum()),
        ('full_width_image', FullWidthImage()),
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
                FieldPanel('use_inverted_menu'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                StreamFieldPanel('body'),
            ],
            heading="Body",
            classname="collapsible collapsed full"
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

    def get_blogposts(self):
        return PostPage.objects.descendant_of(self).live()[:6]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['programs'] = self.get_programs()
        context['blogposts'] = self.get_blogposts()
        context['home_page'] = self
        return context


class ProgramPage(Page):
    programTitle = models.CharField(max_length=255, blank=True, )
    group = models.CharField(max_length=255, blank=True, help_text='Use as: Bachelor of ....')
    detail = models.CharField(max_length=255, blank=True, help_text='Use like: *Pending Aprovement..')
    letters = models.CharField(max_length=5, blank=True, )
    short = RichTextField( help_text='Short description to use in other pages');
    imageBase = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True
    )
    #herocarrousel = StreamField([('item', HeroProgram())], null=True, blank=True)
    #herobanner = StreamField([('large_banner', Banner()),
    #                          ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site"))
    #                          ], null=True, blank=True)

    herocarrousel = StreamField([
        ('academic', HeroAcademic()),
        ('mini_photo', HeroWithMiniFoto()),
        ('solo_text', HeroSoloText()),
        ('photo_or_letters', HeroWithFotoOrLetter()),
        ('with_parameters', HeroParametric()),
    ], null=True, blank=True)

    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
                              ], null=True, blank=True)

    use_inverted_menu = models.BooleanField(default=False, help_text="Invert the color of the Top Menu")

    body = StreamField([
        ('central_circle', CentralCircle(icon="radio-empty")),
        #('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs", icon="site")),
        ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post", icon="site")),
        ('full_text', FullText()),
        ('two_columns_aum', TwoColumnAum()),
        ('separator_arrow', SeparatorLittleArrow()),
        ('circle_key_values', CircleKeyValues()),
        ('circle_apply_banner', CircleApplyBanner()),
        ('fast_full_text', FastFullText()),
        ('big_numbers_text', BigNumbersText()),
        ('group_cards', GroupCards()),
        ('two_columns_inverted', TwoColumnsInverted()),
        ('professor_list', MiniProfessorList()),
        ('round_frame_text', RoundFrameText()),
        ('vertical_paragraph', VerticalParagraph()),
        ('vertical_paragraph_complex', VerticalParagraphComp()),
        ('mini_apply_alone', MiniApplyAlone()),
        ('anchor', AnchorBlock()),
        ('generic_button', GenericButtonAum()),
        ('full_width_image', FullWidthImage()),
    ], null=True, blank=True)

    effects = StreamField([
        ('pin_color', MagicPinColor()),
        ('unround_carousel', MagicCarouselUnround())
    ], null=True, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('programTitle', classname="full"),
        FieldPanel('group', classname="full"),
        FieldPanel('letters', classname="full"),
        FieldPanel('short', classname="full"),
        ImageChooserPanel('imageBase', classname="full"),
        MultiFieldPanel(
            [
                StreamFieldPanel('herocarrousel'),
                StreamFieldPanel('herobanner'),
                FieldPanel('use_inverted_menu'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('body'),
        MultiFieldPanel(
            [
                StreamFieldPanel('effects'),
            ],
            heading="Effects",
            classname="collapsible collapsed"
        ),
    ]

    def get_programs(self):
        return ProgramPage.objects.live()

    def get_blogposts(self):
        return PostPage.objects.live()[:6]


    def get_context(self, request, *args, **kwargs):
        context = super(ProgramPage, self).get_context(request, *args, **kwargs)
        context['programs'] = self.get_programs()
        context['blogposts'] = self.get_blogposts()
        context['program_page'] = self
        return context


class ContentPage(Page):
    herocarrousel = StreamField([
                                ('academic', HeroAcademic()),
                                ('mini_photo', HeroWithMiniFoto()),
                                ('solo_text', HeroSoloText()),
                                ('photo_or_letters', HeroWithFotoOrLetter()),
                                ('with_parameters', HeroParametric()),
                                 ], null=True, blank=True)
    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
                              ], null=True, blank=True)

    use_inverted_menu = models.BooleanField(default=False, help_text="Invert the color of the Top Menu")

    body = StreamField([
        ('central_circle', CentralCircle(icon="radio-empty")),
        ('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs", icon="site")),
        ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post", icon="site")),
        ('full_text', FullText()),
        ('fast_full_text', FastFullText()),
        ('two_columns_aum', TwoColumnAumGeneric()),
        ('separator_arrow', SeparatorLittleArrow()),
        ('circle_key_values', CircleKeyValues()),
        ('circle_apply_banner', CircleApplyBanner()),
        ('big_numbers_text', BigNumbersText()),
        ('group_cards', GroupCards()),
        ('two_columns_inverted', TwoColumnsInverted()),
        ('professor_list', MiniProfessorList()),
        ('round_frame_text', RoundFrameText()),
        ('vertical_paragraph', VerticalParagraph()),
        ('vertical_paragraph_complex', VerticalParagraphComp()),
        ('mini_apply_alone', MiniApplyAlone()),
        ('anchor', AnchorBlock()),
        ('generic_button', GenericButtonAum()),
        ('full_width_image', FullWidthImage()),
        #('form_view', FormView()),
    ], null=True, blank=True)

    effects = StreamField([
        ('pin_color', MagicPinColor()),
        ('unround_carousel', MagicCarouselUnround())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel('herocarrousel'),
                StreamFieldPanel('herobanner'),
                FieldPanel('use_inverted_menu'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('body'),
        MultiFieldPanel(
            [
                StreamFieldPanel('effects'),
            ],
            heading="Effects",
            classname="collapsible collapsed"
        ),
    ]

    def get_programs(self):
        return ProgramPage.objects.live()

    def get_blogposts(self):
        return PostPage.objects.live()[:6]


    def get_context(self, request, *args, **kwargs):
        context = super(ContentPage, self).get_context(request, *args, **kwargs)
        context['programs'] = self.get_programs()
        context['blogposts'] = self.get_blogposts()
        context['content_page'] = self
        return context


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='custom_form_fields')


class FormPage(AbstractEmailForm):
    herocarrousel = StreamField([
        ('academic', HeroAcademic()),
        ('mini_photo', HeroWithMiniFoto()),
        ('solo_text', HeroSoloText()),
        ('photo_or_letters', HeroWithFotoOrLetter()),
        ('with_parameters', HeroParametric()),
    ], null=True, blank=True)
    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
                              ], null=True, blank=True)

    use_inverted_menu = models.BooleanField(default=False, help_text="Invert the color of the Top Menu")

    body = StreamField([
        ('central_circle', CentralCircle(icon="radio-empty")),
        ('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs", icon="site")),
        ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post", icon="site")),
        ('full_text', FullText()),
        ('fast_full_text', FastFullText()),
        ('two_columns_aum', TwoColumnAumGeneric()),
        ('separator_arrow', SeparatorLittleArrow()),
        ('circle_key_values', CircleKeyValues()),
        ('circle_apply_banner', CircleApplyBanner()),
        ('big_numbers_text', BigNumbersText()),
        ('group_cards', GroupCards()),
        ('two_columns_inverted', TwoColumnsInverted()),
        ('professor_list', MiniProfessorList()),
        ('round_frame_text', RoundFrameText()),
        ('vertical_paragraph', VerticalParagraph()),
        ('vertical_paragraph_complex', VerticalParagraphComp()),
        ('mini_apply_alone', MiniApplyAlone()),
        ('form_view', FormView()),
        ('anchor', AnchorBlock()),
        ('generic_button', GenericButtonAum()),
        ('full_width_image', FullWidthImage()),
    ], null=True, blank=True)

    thank_you_body = StreamField([
        ('central_circle', CentralCircle(icon="radio-empty")),
        ('two_columns', TwoColumnBlock()),
        ('vertical_space', VerticalSpace()),
        ('circle_image_block', CircleImageBlock(icon="placeholder")),
        ('big_text_boxes', BigTextBoxes(icon="placeholder")),
        ('carousel_with_banner', CarouselWithBanner(icon="placeholder")),
        ('three_columns_mini', ThreeColumnsMini()),
        ('programs_list', blocks.StaticBlock(label="Show the list of Programs", icon="site")),
        ('blog_list', blocks.StaticBlock(label="Show the list of Blog Post", icon="site")),
        ('full_text', FullText()),
        ('fast_full_text', FastFullText()),
        ('two_columns_aum', TwoColumnAumGeneric()),
        ('separator_arrow', SeparatorLittleArrow()),
        ('circle_key_values', CircleKeyValues()),
        ('circle_apply_banner', CircleApplyBanner()),
        ('big_numbers_text', BigNumbersText()),
        ('group_cards', GroupCards()),
        ('two_columns_inverted', TwoColumnsInverted()),
        ('professor_list', MiniProfessorList()),
        ('round_frame_text', RoundFrameText()),
        ('vertical_paragraph', VerticalParagraph()),
        ('vertical_paragraph_complex', VerticalParagraphComp()),
        ('mini_apply_alone', MiniApplyAlone()),
        ('anchor', AnchorBlock()),
        ('generic_button', GenericButtonAum()),
        ('full_width_image', FullWidthImage()),
        #('form_view', FormView()),
    ], null=True, blank=True)

    effects = StreamField([
        ('pin_color', MagicPinColor()),
        ('unround_carousel', MagicCarouselUnround())
    ], null=True, blank=True)

    #thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        MultiFieldPanel(
            [
                StreamFieldPanel('herocarrousel'),
                StreamFieldPanel('herobanner'),
                FieldPanel('use_inverted_menu'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('body'),
        MultiFieldPanel(
            [
                StreamFieldPanel('effects'),
            ],
            heading="Effects",
            classname="collapsible collapsed"
        ),
        InlinePanel('custom_form_fields', label="Form fields"),
        #FieldPanel('thank_you_text', classname="full"),
        StreamFieldPanel('thank_you_body'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()


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
    talk_to_admission_link = models.CharField(default="",max_length=255,help_text='Url of Representative')
    talk_to_admission_text = RichTextField(default="")
    talk_to_admission_short = models.CharField(default="",max_length=255,help_text='Url of Representative')
    get_leaf_text = RichTextField(default="")
    get_leaf_short = models.CharField(default="", max_length=255, help_text='Url of Representative')
    scholarship_text = RichTextField(default="")
    scholarship_short = models.CharField(default="", max_length=255, help_text='Url of Representative')
    use_wagtail_bar = models.BooleanField(default=False)


@register_setting
class SocialSettings(BaseSetting):
    email = models.CharField(default="",max_length=255, blank=True)
    weburl = models.CharField(default="",max_length=255, blank=True)
    facebook = models.CharField(default="",max_length=255, blank=True)
    twitter = models.CharField(default="",max_length=255,blank=True)


@register_setting
class NavigationMenus(BaseSetting):
    #top = SnippetChooserBlock('home.NavigationMenu', blank=True)
    top = models.ForeignKey(
        'home.NavigationMenu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    footer = models.ForeignKey(
        'home.FooterData',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        SnippetChooserPanel('top'),
        SnippetChooserPanel('footer'),
    ]


@register_snippet
class NavigationMenu(models.Model):
    title = models.CharField(max_length=255, blank=True)
    items = StreamField([
        ('simple', NavigationItem(icon="radio-empty")),
        ('dropdown', NavigationDropdown(icon="radio-empty")),
        ('veritical_separator', blocks.StaticBlock(icon="radio-empty")),
    ], blank=True)

    panels =[
        FieldPanel('title'),
        StreamFieldPanel('items'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


@register_snippet
class FooterData(models.Model):
    title = models.CharField(max_length=255, blank=True)
    items = StreamField([
        ('column', FooterColumn(icon="radio-empty")),
    ], blank=True)

    panels =[
        FieldPanel('title'),
        StreamFieldPanel('items'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"


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




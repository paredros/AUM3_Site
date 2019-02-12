from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.embeds.blocks import EmbedBlock


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


class AnchorBlock(blocks.StructBlock):
    anchor = blocks.CharBlock()

    class Meta:
        template = 'tmps/tmp_anchor.html'
        icon = 'placeholder'
        label = 'Anchor'


class FullWidthImage(blocks.StructBlock):
    image = ImageChooserBlock()
    padding = blocks.CharBlock(default="0px")

    class Meta:
        template = 'tmps/tmp_full_width_image.html'
        icon = 'placeholder'
        label = 'Full Width Image'


class HeroBannerCarrousel(blocks.StructBlock):
    heading = blocks.RichTextBlock()
    image = ImageChooserBlock()
    tintBlue = blocks.FloatBlock(label='Alpha Tint of the Blue Overlay')


class HeroCarouselMulti(blocks.StructBlock):
    items = blocks.StreamBlock([
        ('item',HeroBannerCarrousel())
    ])

    class Meta:
        template = 'tmps/tmp_herocarousel.html'
        icon = 'placeholder'
        label = 'Hero Multi'


class Banner(blocks.StructBlock):
    textType = blocks.ChoiceBlock(choices=[
        ('simple', 'Simple'),
        ('double', 'double'),
    ], icon='edit')
    text = blocks.RichTextBlock()
    text2 = blocks.RichTextBlock()

    class Meta:
        icon = 'user'
        form_classname = 'apply-banner struct-block'


class HeroBannerCircText(blocks.StructBlock):
    text = blocks.RichTextBlock()

    class Meta:
        icon = 'placeholder'
        template = 'tmps/tmp_banner_circ_text.html'


class CircleApplyWithPhoto(blocks.StructBlock):
    idHash = blocks.CharBlock(label='To be identified by script')
    image = ImageChooserBlock()


class VerticalSpace(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=[
        ('nano', 'Nano'),
        ('mini', 'Mini'),
        ('xsmall', 'Xsmall'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], icon='edit')

    class Meta:
        template = 'tmps/tmp_vertical_space.html'


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
    link = blocks.PageChooserBlock(blank=True, null=True, required=False)


class ThreeColumnsMini(blocks.StructBlock):
    column_one = ThreeColumnsMiniItem()
    column_two = ThreeColumnsMiniItem()
    column_three = ThreeColumnsMiniItem()

    class Meta:
        template = 'tmps/tmp_threecolmin.html'
        icon = 'placeholder'
        label = 'Three Columns Mini'


class MagicPinColor(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')
    trigger_hook = blocks.CharBlock(label="Value from 0 to 1 ej: 0.45, or events like onLeave, check Scrollmagic")
    duration = blocks.CharBlock(label="Duration in Pixels ej: 500, or % of screen")
    color_bg = SnippetChooserBlock('home.Colors', blank=True)
    push_followers = blocks.BooleanBlock(required=False)


class CentralCircle(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator', required=False)
    font_color = SnippetChooserBlock('home.Colors', blank=True)
    back_color = SnippetChooserBlock('home.Colors', blank=True)
    text_big = blocks.RichTextBlock(required=False)
    text_line1 = blocks.RichTextBlock(required=False)
    text_line2 = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/tmp_centralcircle_aum.html'


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
    text_big_size = blocks.ChoiceBlock(choices=[
        ('medium', 'Medium'),
        ('big', 'Big'),
    ], icon='edit', default='big')
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    use_banner = blocks.BooleanBlock(required=False)
    use_banner_apply = blocks.BooleanBlock(required=False)
    use_button = blocks.BooleanBlock(required=False)
    link_button = blocks.PageChooserBlock(blank=True, null=True)
    button_text_big = blocks.CharBlock(required=False, label='Fill if you dont use Apply Banner')
    button_text_line1 = blocks.CharBlock(required=False, label='Fill if you dont use Apply Banner')
    button_text_line2 = blocks.CharBlock(required=False, label='Fill if you dont use Apply Banner')
    text_line1 = blocks.RichTextBlock()
    use_round_effect = blocks.BooleanBlock(required=False)

    class Meta:
        template = 'tmps/tmp_carousel_with_banner.html'


class MagicCarouselUnround(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator')
    duration = blocks.CharBlock(default="300",label="Duration in Pixels ej: 500, or % of screen")


class HeroProgram(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')


class HeroAcademic(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')
    letters = blocks.CharBlock(max_length=3, default="AA", label='Initial or Code Letters')
    big_text = blocks.RichTextBlock()
    detail_text = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/tmp_hero_academic.html'


class HeroWithMiniFoto(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')
    mini_image = ImageChooserBlock(required=False)
    big_text = blocks.RichTextBlock()
    size_text = blocks.ChoiceBlock(choices=[
        ('big', 'Big'),
        ('normal', 'Normal'),
    ], icon='edit', default="big")
    detail_text = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/tmp_hero_with_mini_photo.html'


class HeroSoloText(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')
    big_text = blocks.RichTextBlock()
    detail_text = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/tmp_hero_solo_text.html'


class HeroWithFotoOrLetter(blocks.StructBlock):
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ])
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')
    tint_R = blocks.IntegerBlock(default=0)
    tint_G = blocks.IntegerBlock(default=74)
    tint_B = blocks.IntegerBlock(default=135)
    big_text = blocks.RichTextBlock()
    detail_text = blocks.RichTextBlock(required=False)
    use_image = blocks.BooleanBlock(required=False)
    mini_image = ImageChooserBlock(required=False)
    letters = blocks.CharBlock(required=False, max_length=3, label="Initial letters if dont use image")
    letters_color = SnippetChooserBlock('home.Colors', blank=True,required=False)
    letters_back = SnippetChooserBlock('home.Colors', blank=True,required=False)


    class Meta:
        template = 'tmps/tmp_hero_photo_letter.html'


class HeroParametric(blocks.StructBlock):
    use_image_carousel = blocks.BooleanBlock(required=False)
    images = blocks.StreamBlock([
        ('image', ImageChooserBlock())
    ], required=False)
    tint_overlay = blocks.FloatBlock(default=0.7, label='Amount of blue Tint')
    tint_R = blocks.IntegerBlock(default=0)
    tint_G = blocks.IntegerBlock(default=74)
    tint_B = blocks.IntegerBlock(default=135)
    height = blocks.CharBlock(default="300px")
    min_height = blocks.CharBlock(default="500px")
    big_text = blocks.RichTextBlock()
    detail_text = blocks.RichTextBlock(required=False)
    text_color = SnippetChooserBlock('home.Colors', blank=True, required=False)
    use_circle = blocks.BooleanBlock(required=False)
    use_image = blocks.BooleanBlock(required=False)
    mini_image = ImageChooserBlock(required=False)
    letters = blocks.CharBlock(required=False, max_length=3, label="Initial letters if dont use image")
    letters_color = SnippetChooserBlock('home.Colors', blank=True,required=False)
    letters_back = SnippetChooserBlock('home.Colors', blank=True,required=False)


    class Meta:
        template = 'tmps/tmp_hero_params.html'


class FullText(blocks.StructBlock):
    text_size = blocks.ChoiceBlock(choices=[
        ('xsmall', 'X-Small'),
        ('small', 'Small'),
        ('normal', 'Normal'),
        ('medium', 'Medium'),
        ('big', 'Big'),
        ('giant', 'Giant'),
    ], icon='edit', default='big')
    font_color = SnippetChooserBlock('home.Colors', blank=True)
    text = blocks.RichTextBlock()
    align = blocks.CharBlock(default="left", label='css align type [left, right, center, etc]')
    use_container = blocks.BooleanBlock(required=False, default=False)
    use_background_color = blocks.BooleanBlock(required=False)
    back_color = SnippetChooserBlock('home.Colors', blank=True, required=False)
    padding = blocks.CharBlock(default="none", label='css padding value', required=False)
    margin = blocks.CharBlock(default="none", label='css margin value', required=False)

    class Meta:
        template = 'tmps/tmp_full_text.html'


class FastFullText(blocks.StructBlock):
    text_size = blocks.ChoiceBlock(choices=[
        ('xsmall', 'X-Small'),
        ('small', 'Small'),
        ('normal', 'Normal'),
        ('medium', 'Medium'),
        ('big', 'Big'),
        ('giant', 'Giant'),
    ], icon='edit', default='big')
    font_color = SnippetChooserBlock('home.Colors', blank=True)
    text = blocks.RichTextBlock()
    align = blocks.CharBlock(default="left", label='css align type [left, right, center, etc]')
    use_container = blocks.BooleanBlock(required=False, default=False)

    class Meta:
        template = 'tmps/tmp_fast_full_text.html'


class SectionNameProgram(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', required=False)

    class Meta:
        template = 'tmps/tmp_section_name_program.html'
        icon = 'placeholder'
        label = 'Block Name Program'

class SectionButtonsProgram(blocks.StructBlock):
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')
    #link_representative = blocks.CharBlock(label='Url of Representative')
    has_leaflet = blocks.BooleanBlock(required=False)
    link_leaflet = blocks.CharBlock(required=False,label='Url to Leaflet')
    has_scholarship = blocks.BooleanBlock(required=False)
    link_scholarship = blocks.PageChooserBlock(required=False)

    class Meta:
        template = 'tmps/tmp_buttons_program.html'
        icon = 'placeholder'
        label = 'Block Buttons Program'

class SideApplyButton(blocks.StructBlock):
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/tmp_side_apply.html'
        icon = 'placeholder'
        label = 'Side Apply Button'


class TuitionFeeProgram(blocks.StructBlock):
    years = blocks.CharBlock(label='Years Program')
    amount = blocks.CharBlock(default="€15,500*", label='Amount With Symbols (€,*)')
    detail = blocks.CharBlock(default="*Please note: All Maltese and EU Nationals that "
                                      "have resided in Malta for five (5) of the last seven (7)"
                                      " years are eligible for a 50% tuition discount",
                              label='Details')

    class Meta:
        template = 'tmps/tmp_tuition_fee_year.html'
        icon = 'placeholder'
        label = 'Tuition Fee-Year Block'


class SeparatorLittleArrow(blocks.StructBlock):
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/tmp_separetor_arrow.html'
        icon = 'placeholder'
        label = 'Separator Little Arrow'

class PlanOutline_Task(blocks.StructBlock):
    code = blocks.CharBlock(default="", required=False)
    name = blocks.CharBlock(default="")
    credits = blocks.CharBlock(default="", required=False)


class PlanOutline_Year(blocks.StructBlock):
    name_year = blocks.CharBlock(default="Year 1", label='The Year Name')
    semester_1 = blocks.StreamBlock([
        ('program_task', PlanOutline_Task())
    ])
    total_semester_1 = blocks.CharBlock(label='Total Credits For Semester 1')
    semester_2 = blocks.StreamBlock([
        ('program_task', PlanOutline_Task())
    ])
    total_semester_2 = blocks.CharBlock(label='Total Credits For Semester 2')


class PlanOutline(blocks.StructBlock):
    credits = blocks.CharBlock(default="120", label='Credits Total Program')
    years = blocks.StreamBlock([
        ('year_outline', PlanOutline_Year())
    ])

    class Meta:
        template = 'tmps/tmp_planoutline.html'
        icon = 'placeholder'
        label = 'Outline Table for Programs'


class SimpleTableLikeOutline(blocks.StructBlock):
    name_big = blocks.CharBlock(default="", required=False)
    name_sub = blocks.CharBlock(default="", required=False)
    name_sub_mini = blocks.CharBlock(default="", required=False)
    title_column_1 = blocks.CharBlock(default="", required=False)
    title_column_2 = blocks.CharBlock(default="", required=False)
    text_end = blocks.CharBlock(default="", required=False)
    fields = blocks.StreamBlock([
        ('tasks', PlanOutline_Task())
    ])

    class Meta:
        template = 'tmps/tmp_tableoutline.html'
        icon = 'placeholder'
        label = 'Table Like Outline'


class CircleKeyValues(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    background_color = SnippetChooserBlock('home.Colors', blank=True)
    key_value = blocks.StreamBlock([
        ('key_value', blocks.CharBlock())
    ])

    class Meta:
        template = 'tmps/tmp_circle_key_value_aum.html'
        icon = 'placeholder'
        label = 'Little Circles with Value'


class StoryItem(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()


class StoriesBloc(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')
    title = blocks.CharBlock()
    story = blocks.StreamBlock([
        ('story', StoryItem())
    ])

    class Meta:
        template = 'tmps/tmp_stories_aum.html'
        icon = 'placeholder'
        label = 'Stories Block'



class GenericButtonAum(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')
    title = blocks.CharBlock()
    link = blocks.PageChooserBlock(required=False)
    use_external = blocks.BooleanBlock(required=False)
    link_external = blocks.CharBlock(required=False)

    class Meta:
        template = 'tmps/tmp_button_aum.html'
        icon = 'placeholder'
        label = 'Button Aum'



class Comp_TwoBigNumbers(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    text_mini_top = blocks.CharBlock(required=False)
    number_big1 = blocks.CharBlock(required=False)
    text_below1 = blocks.CharBlock(required=False)
    number_big2 = blocks.CharBlock(required=False)
    text_below2 = blocks.CharBlock(required=False)

    class Meta:
        template = 'tmps/comp_twobignumb.html'
        icon = 'placeholder'
        label = 'Two Big Numbers and Text'

class Comp_BigNumbAndText(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    number_big = blocks.CharBlock(required=False)
    text_below1 = blocks.CharBlock(required=False)
    text_big = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/comp_bignumbandtext.html'
        icon = 'placeholder'
        label = 'Big Number and Text'



class Comp_Two_Big_Text(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    text_big1 = blocks.RichTextBlock(required=False)
    text_big2 = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/comp_twobigtext.html'
        icon = 'placeholder'
        label = 'Two Big Text'


class Comp_TextBanner(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    text_big1 = blocks.CharBlock(required=False)
    text_big2 = blocks.RichTextBlock(required=False)
    text_small = blocks.RichTextBlock(required=False)
    has_button = blocks.BooleanBlock(required=False)
    link = blocks.PageChooserBlock(required=False)
    use_external_link = blocks.BooleanBlock(required=False)
    external_link = blocks.CharBlock(required=False)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/comp_textbanner.html'
        icon = 'placeholder'
        label = 'Text Banner'


class Comp_BigNumbAndTextTitle(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    text_mini_color = SnippetChooserBlock('home.Colors', blank=True)
    number_big = blocks.CharBlock(required=False)
    text_normal = blocks.RichTextBlock(required=False)
    text_title = blocks.CharBlock(required=False)

    class Meta:
        template = 'tmps/comp_bignumbtext_title.html'
        icon = 'placeholder'
        label = 'Big Number and Title with Sub'


class Comp_InlineFill_Item(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=[
        ('NormalMini', 'Normal'),
        ('ReallyBig', 'Big'),
        ('ReallyBig', 'Giant'),
    ], icon='edit', default='dark')
    text = blocks.CharBlock()
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    bold = blocks.BooleanBlock(required=False)

class Comp_InlineFill(blocks.StructBlock):
    items = blocks.StreamBlock([
        ('item', Comp_InlineFill_Item()),
    ])
    align_bottom = blocks.BooleanBlock(required=False)

    class Meta:
        template = 'tmps/comp_inline_fill.html'
        icon = 'placeholder'
        label = 'Inline Fill'


class CompositionsBlock(blocks.StructBlock):
    compositions = blocks.StreamBlock([
        ('two_big_numbers', Comp_TwoBigNumbers()),
        ('big_numb_and_text', Comp_BigNumbAndText()),
        ('two_big_text', Comp_Two_Big_Text()),
        ('text_banner', Comp_TextBanner()),
        ('vertical_space', VerticalSpace()),
        ('big_numb_and_title', Comp_BigNumbAndTextTitle()),
        ('inline_text', Comp_InlineFill()),
    ])

    class Meta:
        template = 'tmps/tmp_compositions.html'
        icon = 'placeholder'
        label = 'Compositions Block'


class MiniProfessorItem(blocks.StructBlock):
    name = blocks.CharBlock()
    subtitle = blocks.CharBlock(label="Professor of...")
    use_photo = blocks.BooleanBlock(required=False)
    image = ImageChooserBlock(required=False)
    letters = blocks.CharBlock(required=False, label="Inital Letter like AA if dont use picture")
    letters_color = SnippetChooserBlock('home.Colors', blank=True, required=False)
    letters_back = SnippetChooserBlock('home.Colors', blank=True, required=False)
    link = blocks.PageChooserBlock()




class MiniProfessorList(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')
    items = blocks.StreamBlock([('professor_data',MiniProfessorItem())])

    class Meta:
        template = 'tmps/tmp_miniprofessor.html'
        icon = 'placeholder'
        label = 'Professor List'


class SimpleTableItem(blocks.StructBlock):
    fields = blocks.StreamBlock([('item', blocks.CharBlock())])


class SimpleTableColumnDef(blocks.StructBlock):
    width = blocks.CharBlock(label="From 1 to 12 using Grids (total must be 12)")
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    #items = blocks.StreamBlock([('items', blocks.CharBlock())])


class SimpleTable(blocks.StructBlock):
    columns_def = blocks.StreamBlock([('column_def',SimpleTableColumnDef())])
    records = blocks.StreamBlock([('record',SimpleTableItem())])

    class Meta:
        template = 'tmps/tmp_simple_table.html'
        icon = 'placeholder'
        label = 'Simple Table'


class RoundFrameText(blocks.StructBlock):
    text = blocks.RichTextBlock()
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    back_color = SnippetChooserBlock('home.Colors', blank=True)

    class Meta:
        template = 'tmps/tmp_round_frame_text.html'
        icon = 'placeholder'
        label = 'Round Frame Text'


class VerticalParagraph(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    blocks = blocks.StreamBlock(
        [('text_block',blocks.CharBlock())]
    )

    class Meta:
        template = 'tmps/tmp_vertical_para.html'
        icon = 'placeholder'
        label = 'Vertical Plain Paragraph'


class VerticalParagraphItem(blocks.StructBlock):
    big_text = blocks.CharBlock(required=False)
    normal_text = blocks.CharBlock(required=False)
    big_text_color = SnippetChooserBlock('home.Colors', blank=True)
    normal_text_color = SnippetChooserBlock('home.Colors', blank=True)


class VerticalParagraphComp(blocks.StructBlock):
    blocks = blocks.StreamBlock(
        [('block', VerticalParagraphItem())]
    )

    class Meta:
        template = 'tmps/tmp_vertical_para_complex.html'
        icon = 'placeholder'
        label = 'Vertical Paragraph Complex'


class YoutubeBlock(blocks.StructBlock):
    video = blocks.CharBlock()

    class Meta:
        template = 'tmps/tmp_youtube.html'
        icon = 'placeholder'
        label = 'Youtube Video'


class AccordionItem(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.RichTextBlock()


class AccordionBlock(blocks.StructBlock):
    anchor = blocks.CharBlock()
    items = blocks.StreamBlock([
        ("item", AccordionItem())
    ])
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')
    title_text_color = SnippetChooserBlock('home.Colors', blank=True)
    body_text_color = SnippetChooserBlock('home.Colors', blank=True)
    body_back_color = SnippetChooserBlock('home.Colors', blank=True)


    class Meta:
        template = 'tmps/tmp_accordion.html'
        icon = 'placeholder'
        label = 'Accordion Block'


class SimpleRecordsItem(blocks.StructBlock):
    field_left = blocks.CharBlock()
    field_right = blocks.CharBlock()
    field_detail = blocks.CharBlock(required=False)


class SimpleRecordsTable(blocks.StructBlock):
    field_text_color = SnippetChooserBlock('home.Colors', blank=True)
    detail_text_color = SnippetChooserBlock('home.Colors', blank=True)
    items = blocks.StreamBlock([
        ('record', SimpleRecordsItem()),
    ])

    class Meta:
        template = 'tmps/tmp_simple_records.html'
        icon = 'placeholder'
        label = 'Simple Records Table'


class FormView(blocks.StructBlock):
    #text_color = SnippetChooserBlock('home.Colors', blank=True)
    use_container = blocks.BooleanBlock(required=False)
    use_simple_button = blocks.BooleanBlock(required=False, default=True)
    text_submit = blocks.CharBlock(default="Submit")
    text_submit_2 = blocks.CharBlock(default="Send", label="Only for complex button")

    class Meta:
        template = 'tmps/tmp_form_view.html'
        icon = 'placeholder'
        label = 'Form View (only Form Page)'


class SocialButtons(blocks.StructBlock):
    show_email = blocks.BooleanBlock(required=False, default=True)
    show_web = blocks.BooleanBlock(required=False, default=True)
    show_facebook = blocks.BooleanBlock(required=False, default=True)
    show_twitter = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        template = 'tmps/tmp_social.html'
        icon = 'placeholder'
        label = 'Social Buttons'


class GoogleMap(blocks.StructBlock):
    lat = blocks.CharBlock(default="35.881718")
    lng = blocks.CharBlock(default="14.519760")
    zoom = blocks.CharBlock(default="15")

    class Meta:
        template = 'tmps/tmp_map.html'
        icon = 'placeholder'
        label = 'Google Map'


class LeftColumnAum(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    program_name = SectionNameProgram()
    buttons_program = SectionButtonsProgram()
    vertical_space = VerticalSpace()
    side_apply_button = SideApplyButton()
    generic_button = GenericButtonAum()

    class Meta:
        template = 'tmps/tmp_leftcolumn_aum.html'


class LeftColumnAumGeneric(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    buttons_program = SectionButtonsProgram()
    vertical_space = VerticalSpace()
    side_apply_button = SideApplyButton()
    fast_text = FastFullText()
    full_text = FullText()
    generic_button = GenericButtonAum()
    form_view = FormView()
    social_buttons = SocialButtons()


    class Meta:
        template = 'tmps/tmp_leftcolumn_aum.html'


class RightColumnAum(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    tuition_fee_block = TuitionFeeProgram()
    full_text = FullText()
    vertical_space = VerticalSpace()
    separator_arrow = SeparatorLittleArrow()
    plan_outline = PlanOutline()
    stories_block = StoriesBloc()
    generic_button = GenericButtonAum()
    anchor = AnchorBlock()
    full_width_image = FullWidthImage()

    class Meta:
        template = 'tmps/tmp_rightcolumn_aum.html'


class RightColumnAumGeneric(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    full_text = FullText()
    fast_full_text = FastFullText()
    vertical_space = VerticalSpace()
    separator_arrow = SeparatorLittleArrow()
    stories_block = StoriesBloc()
    plan_outline = PlanOutline()
    tuition_fee_block = TuitionFeeProgram()
    table_like_outline = SimpleTableLikeOutline()
    compositions_block = CompositionsBlock()
    simple_table = SimpleTable()
    #embed = EmbedBlock()
    youtube = YoutubeBlock()
    accordion_block = AccordionBlock()
    simple_records = SimpleRecordsTable()
    form_view = FormView()
    google_map = GoogleMap()
    anchor = AnchorBlock()
    generic_button = GenericButtonAum()
    full_width_image = FullWidthImage()

    class Meta:
        template = 'tmps/tmp_rightcolumn_aum.html'



class TwoColumnAum(blocks.StructBlock):

    left_column = LeftColumnAum(icon='arrow-left', label='Left column content')
    right_column = RightColumnAum(icon='arrow-right', label='Right column content')
    separator_color = SnippetChooserBlock('home.Colors', blank=True)
    main_text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/tmp_twocolumns_aum.html'
        icon = 'placeholder'
        label = 'Two Columns Aum'


class TwoColumnAumGeneric(blocks.StructBlock):

    left_column = LeftColumnAumGeneric(icon='arrow-left', label='Left column content')
    right_column = RightColumnAumGeneric(icon='arrow-right', label='Right column content')
    separator_color = SnippetChooserBlock('home.Colors', blank=True)
    main_text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/tmp_twocolumns_aum.html'
        icon = 'placeholder'
        label = 'Two Columns Aum'


class CircleApplyBanner(blocks.StructBlock):
    anchor = blocks.CharBlock(label='Id of object to use as activator', required=False)

    class Meta:
        template = 'tmps/tmp_cicleapply_aum.html'
        icon = 'radio-empty'
        label = 'Circle Apply'


class BigNumbersText(blocks.StructBlock):
    numbers_1 = blocks.CharBlock()
    numbers_1_sub = blocks.CharBlock(required=False)
    numbers_2 = blocks.CharBlock()
    numbers_2_sub = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'tmps/tmp_bignumberstext.html'
        icon = 'placeholder'
        label = 'Big Number and Text'


class CardItem(blocks.StructBlock):
    text = blocks.RichTextBlock()
    index = blocks.CharBlock(required=False, label='A Number o Letter Bellow')


class GroupCards(blocks.StructBlock):
    text_color = SnippetChooserBlock('home.Colors', blank=True)
    index_color = SnippetChooserBlock('home.Colors', blank=True)
    background_color = SnippetChooserBlock('home.Colors', blank=True)

    cards = blocks.StreamBlock([
        ('card', CardItem())
    ])

    class Meta:
        template = 'tmps/tmp_groupcards.html'
        icon = 'placeholder'
        label = 'Group Cards'


class TwoColumnsInverted(blocks.StructBlock):
    left_column = RightColumnAumGeneric(icon='arrow-right', label='Left column content')
    right_column = LeftColumnAumGeneric(icon='arrow-left', label='Right column content')
    separator_color = SnippetChooserBlock('home.Colors', blank=True)
    main_text_color = SnippetChooserBlock('home.Colors', blank=True)
    theme = blocks.ChoiceBlock(choices=[
        ('dark', 'Dark'),
        ('white', 'White'),
    ], icon='edit', default='dark')

    class Meta:
        template = 'tmps/tmp_twocolumns_inv.html'
        icon = 'placeholder'
        label = 'Two Columns Inverted'


class MiniApplyAlone(blocks.StaticBlock):

    class Meta:
        template = 'tmps/tmp_mini_apply_alone.html'
        icon = 'placeholder'
        label = 'Mini Apply Button'


class NavigationItem(blocks.StructBlock):
    title = blocks.CharBlock()
    page = blocks.PageChooserBlock(required=False)
    use_external = blocks.BooleanBlock(required=False)
    link_external = blocks.CharBlock(required=False)
    use_anchor = blocks.BooleanBlock(required=False)
    anchor = blocks.CharBlock(required=False, label="like #anchor, dont include #")


class NavigationDropdown(blocks.StructBlock):
    title = blocks.CharBlock()
    items = blocks.StreamBlock([
        ('item', NavigationItem()),
        ('separator', blocks.StaticBlock()),
    ])


class FooterForm(blocks.StructBlock):
    text = blocks.CharBlock()
    form_destination = blocks.PageChooserBlock(target_model="home.FormPage")
    slug_name = blocks.CharBlock(label="the-name-of-the-field (like this)")
    type = blocks.ChoiceBlock(choices=[
        ('email', 'Email'),
        ('text', 'Single Line'),
        ('password', 'Passwor'),
    ], icon='edit', default='email')


class FooterGroup(blocks.StructBlock):
    title = blocks.CharBlock()
    items = blocks.StreamBlock([
        ('item', NavigationItem()),
        ('blank', blocks.StaticBlock()),
        ('text', blocks.StaticBlock()),
        ('social', SocialButtons()),
        ('field_form', FooterForm()),
    ])


class FooterColumn(blocks.StructBlock):
    size = blocks.IntegerBlock(label="grid based, total must be 12")
    content = blocks.StreamBlock([
        ('group', FooterGroup()),
        ('blank', blocks.StaticBlock()),
    ])
import datetime

from django.db import models
from django import forms
from django.http import Http404
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
from wagtail.contrib.routable_page.models import route

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel,
                                         )
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.tags import ClusterTaggableManager

from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from home.models import *
from home.blocks import *

# Create your models here.
class BlogPage(RoutablePageMixin, Page):
    description = models.CharField(max_length=255, blank=True,)

    herocarrousel = StreamField([
        ('academic', HeroAcademic()),
        ('mini_photo', HeroWithMiniFoto()),
        ('solo_text', HeroSoloText()),
        ('photo_or_letters', HeroWithFotoOrLetter()),
    ], null=True, blank=True)

    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
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
    ]

    def get_posts(self):
        return PostPage.objects.descendant_of(self).live().order_by('-date')

    def use_paginator(self, request, post_t):
        page_n = request.GET.get('page')
        if not page_n:
            page_n = "1"
        #post_t = PostPage.objects.descendant_of(self).live().order_by('-date')
        paginator = Paginator(post_t, 6)
        posts_page = paginator.get_page(page_n)
        return posts_page

    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['posts'] = self.posts
        #context['posts'] = self.get_posts
        #context['posts'] = PostPage.objects.descendant_of(self).live()
        context['blog_page'] = self
        context['showing_all'] = self.showing_all
        return context

    @route(r'^view_all/')
    def view_all(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        self.showing_all = True
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.showing_all = False
        self.search_type = 'tag'
        self.search_term = tag
        posts_p = self.get_posts().filter(tags__slug=tag)
        self.posts = self.use_paginator(request, posts_p)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        self.showing_all = False
        self.search_type = 'category'
        self.search_term = category
        posts_p = self.get_posts().filter(categories__slug=category)
        self.posts = self.use_paginator(request, posts_p)
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^author/(?P<author>[-\w]+)/$')
    def post_by_author(self, request, author, *args, **kwargs):
        self.showing_all = False
        self.search_type = 'author'
        self.search_term = author
        posts_p = self.get_posts().filter(author__slug=author)
        self.posts = self.use_paginator(request, posts_p)
        #self.posts = self.get_posts()
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^(\d{4})/$')
    @route(r'^(\d{4})/(\d{2})/$')
    @route(r'^(\d{4})/(\d{2})/(\d{2})/$')
    def post_by_date(self, request, year, month=None, day=None, *args, **kwargs):
        self.showing_all = False
        self.posts = self.get_posts().filter(date__year=year)
        if month:
            self.posts = self.posts.filter(date__month=month)
            df = DateFormat(date(int(year), int(month), 1))
            self.search_term = df.format('F Y')
        if day:
            self.posts = self.posts.filter(date__day=day)
            self.search_term = date_format(date(int(year), int(month), int(day)))
        return Page.serve(self, request, *args, **kwargs)

    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$')
    def post_by_date_slug(self, request, year, month, day, slug, *args, **kwargs):
        post_page = self.get_posts().filter(slug=slug).first()
        self.showing_all = False
        if not post_page:
            raise Http404
        return Page.serve(post_page, request, *args, **kwargs)

    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        #page_n = request.GET.get('page')
        #if not page_n:
        #    page_n = "1"
        #post_t = self.get_posts()
        #paginator = Paginator(post_t, 3)
        #posts_page = paginator.get_page(page_n)
        #self.posts = posts_page
        #self.posts = self.get_posts()
        self.showing_all = False
        posts_p = self.get_posts()
        self.posts = self.use_paginator(request, posts_p)

        return Page.serve(self, request, *args, **kwargs)

"""
class ViewAll(Page):
    herocarrousel = StreamField([
        ('academic', HeroAcademic()),
        ('mini_photo', HeroWithMiniFoto()),
        ('solo_text', HeroSoloText()),
        ('photo_or_letters', HeroWithFotoOrLetter()),
    ], null=True, blank=True)

    herobanner = StreamField([('large_banner', Banner()),
                              ('circle_banner', blocks.StaticBlock(label="Middle Circle Apply", icon="site")),
                              ('mini_banner', blocks.StaticBlock(label="Mini Circle Apply", icon="site")),
                              ('only_text', HeroBannerCircText(label="Only Text Circle", icon="site")),
                              ('circle_talk', blocks.StaticBlock(label="Middle Circle Talk", icon="site")),
                              ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                StreamFieldPanel('herocarrousel'),
                StreamFieldPanel('herobanner'),
            ],
            heading="Hero",
            classname="collapsible collapsed"
        ),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ViewAll, self).get_context(request, *args, **kwargs)
        context['posts'] = self.posts
        #context['posts'] = self.get_posts
        #context['posts'] = PostPage.objects.descendant_of(self).live()
        context['blog_page'] = self
        return context
"""

class PostPage(Page):
    summary = RichTextField(blank=True)
    image_big = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('embedded_video', EmbedBlock(icon="media")),
    ])
    date = models.DateTimeField(verbose_name="Post date", default=datetime.datetime.today)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)
    #author = SnippetChooserBlock('blog.Authors', blank=True)
    author = models.ForeignKey(
        'blog.Authors', on_delete=models.PROTECT, related_name='+',
        blank=True, null=True
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image_big', classname="full"),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
        SnippetChooserPanel('author'),
    ]

    @property
    def blog_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(PostPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self.blog_page
        context['post'] = self
        return context



@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='post_tags')


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

@register_snippet
class Authors(models.Model):
    name = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)
    #slug = models.SlugField(max_length=80, default="name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"



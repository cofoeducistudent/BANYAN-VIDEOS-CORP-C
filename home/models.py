from django.db import models

# Create your models here.
from django.contrib import admin
from django.db import models

# Create your models here.


class FrontPageCarousel(models.Model):

    class Meta:
        verbose_name_plural = "Carousel Images"

    c_item = models.IntegerField(null=True, blank=True)
    c_name = models.CharField(max_length=254, null=True, blank=True)
    c_url = models.URLField(max_length=254, null=True, blank=True)

    def __int__(self):
        return self.c_item


class Article(models.Model):

    class Meta:
        verbose_name_plural = "Articles"

    article_name = models.CharField(max_length=254, null=True, blank=True)
    article_friendly_name = models.CharField(
        max_length=254, null=True, blank=True)
    article_image = models.URLField(max_length=254, null=True, blank=True)
    article_content = models.TextField(max_length=2000, null=True, blank=True)
    article_live = models.BooleanField(default=True)

    def __str__(self):
        return self.article_name


class Snippet(models.Model):
    class Meta:
        verbose_name_plural = "Snippets"
    snippet_name = models.CharField(max_length=254, null=True, blank=True)
    snippet_friendly_name = models.CharField(
        max_length=254, null=True, blank=True)
    snippet_detail = models.TextField(null=True, blank=True)
    snippet_image = models.URLField(max_length=254, null=True, blank=True)
    snippet_source_url = models.URLField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.snippet_name

 

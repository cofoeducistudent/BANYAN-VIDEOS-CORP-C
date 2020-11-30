from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import FrontPageCarousel, Article, Snippet

# Register your models here.

class FrontPageCarouselAdmin(admin.ModelAdmin):
    list_display = ('c_item','c_name', 'c_url')

    ordering = ('c_item',)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_live', 'article_name', 'article_friendly_name', 'article_image' )

    ordering = ('article_name', )
    
class SnippetAdmin(admin.ModelAdmin):
    list_display=('snippet_name','snippet_friendly_name','snippet_image','snippet_source_url')
    
    ordering =('snippet_name', )

 
    
 

admin.site.register(FrontPageCarousel, FrontPageCarouselAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Snippet, SnippetAdmin)
 
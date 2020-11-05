 
from django.contrib import admin
from .models import Films, Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display =(
        
                'genre_name',
                'genre_friendly_name',
    )
    
    ordering = ( 'genre_friendly_name', )




class FilmsAdmin(admin.ModelAdmin):
    list_display = ( 
                    'film_sku',
                    'film_genre',
                    'film_title',
                    'film_friendly_title',
                    'film_box_cover_url',
                    # 'film_description',
                    'film_price',
                    'film_product_discount',
                    'film_stock_available',
                    'film_global_sale',
                    'film_clip_link',
                    
                    )
    
    ordering = ( 'film_title', )
    

admin.site.register(Genre, GenreAdmin)
admin.site.register(Films, FilmsAdmin)

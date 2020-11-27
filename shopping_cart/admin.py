from django.contrib import admin
from .models import ShoppingCartModel
from home import models as home_models

# Register your models here.


class ShoppingCartModelAdmin(admin.ModelAdmin):
    list_display = (

        # 'cart_purchase_date',
        'cart_owner',
        'cart_session',
        'cart_film_quantity',
        'cart_film_genre',
        'cart_film_sku',
        'cart_film_title',
        'cart_film_friendly_title',
        'cart_film_box_cover_url',
        # 'cart_film_description',
        'cart_film_price',
        'cart_film_product_discount',
        'cart_price_paid',
        'cart_film_stock_available',
        'cart_film_global_sale',
        'cart_film_clip_link',

    )

    ordering = ('cart_film_title', )


# admin.site.register(Genre, GenreAdmin)
admin.site.register(ShoppingCartModel, ShoppingCartModelAdmin)

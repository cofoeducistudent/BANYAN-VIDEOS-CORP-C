from django.contrib import admin
from .models import UserProfile
from .models import UserPurchaseHistory

from .models import Genre
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (

        'up_username',
        'up_first_name',
        'up_last_name',
        'up_email',
        'up_address_line1',
        'up_address_line2',
        'up_address_line3',
        'up_post_code',
        'up_country',

    )
    ordering = ('up_username',)


class UserPurchaseHistoryAdmin(admin.ModelAdmin):

    list_display = (

    'ph_purchase_date',
    'ph_cart_owner',
    'ph_transaction_id',
    'ph_cart_film_quantity',
    'ph_cart_price_paid',
    'ph_cart_film_genre',
    'ph_cart_film_sku',
    'ph_cart_film_title',
    'ph_cart_film_friendly_title',
    'ph_cart_film_box_cover_url',
    'ph_cart_film_description',
    'ph_cart_film_price',
    'ph_cart_film_product_discount',

    )

    ordering = ('ph_cart_owner',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserPurchaseHistory, UserPurchaseHistoryAdmin)

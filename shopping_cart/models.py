from datetime import date, datetime
from django.db import models
from django.contrib import sessions

from search_results.models import Genre
# from shopping_cart.views import ShoppingCart
from django.db  import models
from home import models as home_models


# Create your models here.


class ShoppingCartModel(models.Model):
    class Meta:
        verbose_name_plural ="Shopping Cart"
    
    cart_owner = models.CharField(max_length=20, null=True, blank=True)
    cart_session = models.CharField(max_length=128, null=True, blank= True)
    cart_film_quantity= models.IntegerField(default=1, null=True, blank=True)
    cart_price_paid =models.DecimalField(max_digits=5, decimal_places=2, default= 0.00)

    cart_film_genre = models.ForeignKey(Genre, default=1, on_delete=models.SET_DEFAULT)
    cart_film_sku = models.CharField(max_length=128, null= True, blank=True)
    
    cart_film_title = models.CharField(max_length=128, null= True, blank=True)
    cart_film_friendly_title = models.CharField(max_length=254, null=True, blank=True )
    
    cart_film_box_cover_url = models.URLField(max_length=254,default="")
    
    cart_film_description = models.TextField(max_length = 2000, null = True, blank = True)
    
    
    cart_film_price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    cart_film_product_discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00) 
    cart_film_stock_available = models.BooleanField(default=True)
    cart_film_global_sale = models.BooleanField(default=True)
    cart_film_clip_link = models.URLField(max_length=254, null=True, blank=True)
    
    cart_purchase_date = models.CharField(max_length=128, null=True, blank=True)
    
    def __str__(self):
        return self.cart_film_friendly_title
    
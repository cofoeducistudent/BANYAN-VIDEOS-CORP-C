from django.db import models

# Create your models here.


class Genre(models.Model):
    class Meta:
        verbose_name ='Genre'
    
    genre_name = models.CharField(max_length=254, null=True, blank=True)
    genre_friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.genre_name
    
    
    
class Films(models.Model):
    class Meta:
        verbose_name_plural = "Films"
    
    film_sku=models.CharField(max_length=100,null=True,blank=True)
    film_genre=models.ForeignKey(Genre, default=1, on_delete=models.SET_DEFAULT)
    
    film_title = models.CharField(max_length=254, null=True, blank=True )
    film_friendly_title = models.CharField(max_length=254, null=True, blank=True )
    film_box_cover_url = models.URLField(max_length=254,default="")
    film_description = models.TextField(max_length=2000, null=True, blank=True)
    film_price=models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    film_product_discount=models.DecimalField(max_digits=4, decimal_places=2, default=0.00) 
    film_stock_available=models.BooleanField(default=True)
    film_global_sale=models.BooleanField(default=True)
    film_clip_link=models.URLField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.film_friendly_title
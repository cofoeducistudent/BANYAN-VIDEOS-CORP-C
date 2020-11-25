from django.db.models.fields import DateField
from _banyanvideos_root.settings import MEDIA_ROOT
from django.db import models
from search_results.models  import  Genre
# from my_account.models  import UserPurchaseHistory

# Create your models here.





class UserProfile(models.Model):
    class Meta: verbose_name_plural = "User Profiles"
 
    up_username = models.CharField( max_length=254, null=True, blank=True)
    up_first_name = models.CharField( max_length=254, null=True, blank=True)
    up_last_name = models.CharField( max_length=254, null=True, blank=True)

    up_email = models.EmailField( max_length=254, null=True, blank=True)
    up_address_line1 = models.CharField( max_length=254, null=True, blank=True)
    up_address_line2 = models.CharField( max_length=254, null=True, blank=True)
    up_address_line3 = models.CharField( max_length=254, null=True, blank=True)
    up_post_code = models.CharField( max_length=254, null=True, blank=True)
    up_country = models.CharField( max_length=254, null=True, blank=True)
        
    def __str__(self):
        return self.up_username
    
    
    
    
    
    
    
    
class UserPurchaseHistory(models.Model):
    class Meta: verbose_name_plural = "User Purchase History"
    
    
    ph_purchase_date = models.CharField(max_length=20, null=True, blank=True)
    ph_cart_owner = models.CharField(max_length=128, null=True, blank= True)
    ph_transaction_id=models.CharField(max_length=128, null=True, blank=True)
    ph_cart_film_quantity = models.IntegerField(default=1, null=True, blank=True)
    ph_cart_price_paid =models.DecimalField(max_digits=5, decimal_places=2, default= 0.00)
    ph_cart_film_genre = models.ForeignKey(Genre, default=1, on_delete=models.SET_DEFAULT)
    ph_cart_film_sku = models.CharField(max_length=128, null= True, blank=True)
    ph_cart_film_title = models.CharField(max_length=128, null= True, blank=True)
    ph_cart_film_friendly_title = models.CharField(max_length=254, null=True, blank=True )
    ph_cart_film_box_cover_url = models.URLField(max_length=254,default="")
    ph_cart_film_description = models.TextField(max_length = 2000, null = True, blank = True)
    ph_cart_film_price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    ph_cart_film_product_discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00) 
     
    def __str__(self):
        return self.ph_cart_owner
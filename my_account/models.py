from _banyanvideos_root.settings import MEDIA_ROOT
from django.db import models

# Create your models here.





class UserProfile(models.Model):
    class Meta: verbose_name_plural = "UserProfiles"
     
    profile_username = models.CharField(max_length=128, null=True, blank=True),
    profile_address =models.TextField(max_length=2000, null=True ),
    profile_postecode=models.CharField(max_length=20, null=True, blank=True),     
     
    def __str__(self):
        return self.profile_username
    
    
class UserPurchaseHistory(models.Model):
    class Meta: verbose_name_plural = "UserProfiles"
     
    purchase_username = models.CharField(max_length=128, null=True, blank=True),
    purchase_date =models.CharField(max_length=128, null=True, blank=True),
    profile_postecode=models.CharField(max_length=20, null=True, blank=True),     
    
    
 
    purchase_history_owner = models.CharField(max_length=20, null=True, blank=True)
    purchase_history_session = models.CharField(max_length=128, null=True, blank= True)
    purchase_history_film_quantity= models.IntegerField(default=1, null=True, blank=True)
    purchase_history_price_paid =models.DecimalField(max_digits=5, decimal_places=2, default= 0.00)

    # purchase_history_film_genre = models.ForeignKey(Genre, default=1, on_delete=models.SET_DEFAULT)
    purchase_history_film_sku = models.CharField(max_length=128, null= True, blank=True)
    
    purchase_history_film_title = models.CharField(max_length=128, null= True, blank=True)
    purchase_history_film_friendly_title = models.CharField(max_length=254, null=True, blank=True )
    
    purchase_history_film_box_cover_url = models.URLField(max_length=254,default="")
    
    purchase_history_film_description = models.TextField(max_length = 2000, null = True, blank = True)
    
    
    purchase_history_film_price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
    purchase_history_film_product_discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00) 
 
    
    
    
    
    
    
    
     
    def __str__(self):
        return self.profile_username
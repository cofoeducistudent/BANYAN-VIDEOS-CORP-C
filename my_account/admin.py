from django.contrib import admin

from .models    import  UserProfile
from .models    import  UserPurchaseHistory
# Register your models here.



class   UserProfileAdmin(admin.ModelAdmin):
        list_display =(
        
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
        ordering=('up_username',)
        
admin.site.register(UserProfile, UserProfileAdmin)
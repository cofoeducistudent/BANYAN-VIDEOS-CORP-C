from django.contrib import admin

from .models    import  LoginMessages

# Register your models here.


class   LoginMessagesAdmin(admin.ModelAdmin):
    list_display = ('message_date',
                    'messages_visible',
                    'message_title',
                    'message_content')
    
    ordering = ('message_date',)    
    

admin.site.register ( LoginMessages, LoginMessagesAdmin)

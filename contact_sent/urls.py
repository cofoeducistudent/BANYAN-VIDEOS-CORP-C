from contact.views import Contact
from django.urls   import path
from .views import  ContactSent


urlpatterns = [
    
    path('contact', ContactSent.as_view(), name = 'contact_sent'),
              
              ]
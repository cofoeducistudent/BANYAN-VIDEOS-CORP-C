import django
from login_register.views import LoginRegister
from django.views.generic.base import View
from home import views
from django.urls    import path

from .import views




urlpatterns = [
    
    
    
    path('login_register', LoginRegister.as_view(), name="login_register")
              
        
                 
              ]
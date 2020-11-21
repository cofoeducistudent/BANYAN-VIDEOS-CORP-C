import django
from django.urls.conf import include
from login_register.views import LoginRegister
from django.views.generic.base import View
from home import views
from django.urls    import path

 







urlpatterns = [
    
    
  
    
    path('login_register', LoginRegister.as_view(), name="login_register"),
              
 
       
                 
              ]
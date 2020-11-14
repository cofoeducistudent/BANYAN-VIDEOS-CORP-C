from logout.views import Logout
import home
from django.urls import path
from .import views


urlpatterns = [
    
    
    path('logout', Logout.as_view(), name='logout'),
 
  
              ]
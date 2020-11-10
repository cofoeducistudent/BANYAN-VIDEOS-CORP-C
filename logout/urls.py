from django.urls import path
from .views import Logout


urlpatterns = [
    
    path('logout', Logout.as_view(), name="logout"),
  
  
  
              ]
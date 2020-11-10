
from about.views    import AboutView
from django.urls    import  path


urlpatterns = [
    
    path('about', AboutView.as_view(), name = 'about'),
              
              ]